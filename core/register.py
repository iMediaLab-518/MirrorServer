import math
import pickle

from imutils.video import VideoStream
import imutils
import time
import cv2
import os
import os.path
import configparser
import time

from sklearn import neighbors
from utils import image_files_in_folder
import face_recognition

config = configparser.ConfigParser()
config.read("config.ini")

cascade_path = config['global']['cascade']
dataset_dir = config['global']['dataset']
train_dir = os.path.join(dataset_dir, 'train')
model_path = config['global']['modelpath']
VIDEO_TIME = 20  # time of audio


def handle_pic(orig):
    orig = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
    orig = cv2.resize(orig, (320, 240), interpolation=cv2.INTER_AREA)
    return orig


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def train(train_dir, model_save_path=None, n_neighbors=None, knn_algo='ball_tree', verbose=False):
    X = []
    y = []

    for class_dir in os.listdir(train_dir):
        if not os.path.isdir(os.path.join(train_dir, class_dir)):
            continue

        for img_path in image_files_in_folder(os.path.join(train_dir, class_dir)):
            image = face_recognition.load_image_file(img_path)
            face_bounding_boxes = face_recognition.face_locations(image)

            if len(face_bounding_boxes) != 1:
                if verbose:
                    print("Image {} not suitable for training: {}".format(img_path, "Didn't find a face" if len(
                        face_bounding_boxes) < 1 else "Found more than one face"))
            else:
                X.append(face_recognition.face_encodings(image, known_face_locations=face_bounding_boxes)[0])
                y.append(class_dir)

    if n_neighbors is None:
        n_neighbors = int(round(math.sqrt(len(X))))
        if verbose:
            print("Chose n_neighbors automatically:", n_neighbors)

    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=knn_algo, weights='distance')
    knn_clf.fit(X, y)

    # Save the trained KNN classifier
    if model_save_path is not None:
        with open(model_save_path, 'wb') as f:
            pickle.dump(knn_clf, f)

    return knn_clf


def register(person):
    person_dir = '{train_dir}/{person}'.format(train_dir=train_dir, person=person)
    if not os.path.exists(person_dir):
        os.mkdir(person_dir)

    total = len(os.listdir(person_dir))  # pics number existed

    start=time.time()
    detector = cv2.CascadeClassifier(cascade_path)
    vs = VideoStream(src=0).start()

    print("Initlize the camera with {} s".format(time.time()-start))
    start=time.time()

    while True:
        if time.time() - start >= VIDEO_TIME:
            break
        frame = vs.read()
        orig = frame.copy()
        frame = imutils.resize(frame, width=400)

        rects = detector.detectMultiScale(
            cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.1,
            minNeighbors=5, minSize=(30, 30))

        # for (x, y, w, h) in rects:
        #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # coordinate of every face

        cur_person_number = len(rects)
        if cur_person_number == 0:
            # print("Forward")
            pass
            # TODO : Frontend
        elif cur_person_number > 1:
            # print("Wait!")
            pass
            # TODO : Frontend
        else:
            pic_path = os.path.sep.join([person_dir, "{}.png".format(str(total).zfill(5))])

            orig = handle_pic(orig)
            cv2.imwrite(pic_path, orig)
            total += 1
            print("Successful! Current : {}".format(total))

        # cv2.imshow("Frame", frame)
        # key = cv2.waitKey(1) & 0xFF
        # Wait for press

    if not os.path.exists(train_dir):
        os.mkdir(train_dir)

    start=time.time()
    print("[INFO] Start training the pictures!")
    train(train_dir, model_save_path=model_path, n_neighbors=2)
    print("[INFO] Train complete with {} s".format(time.time()-start))

    cv2.destroyAllWindows()
    vs.stop()
