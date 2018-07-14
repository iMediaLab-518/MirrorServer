import os
import pickle

import cv2
import time
import configparser
import face_recognition

config = configparser.ConfigParser()
config.read("config.ini")

dataset_dir = config['global']['dataset']
model_path = config['global']['modelpath']
pic_filename = 'unknown.png'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def predict(X_img_path, knn_clf=None, model_path=None, distance_threshold=0.4):
    if not os.path.isfile(X_img_path) or os.path.splitext(X_img_path)[1][1:] not in ALLOWED_EXTENSIONS:
        raise Exception("Invalid image path: {}".format(X_img_path))

    if knn_clf is None and model_path is None:
        raise Exception("Must supply knn classifier either thourgh knn_clf or model_path")

    if knn_clf is None:
        with open(model_path, 'rb') as f:
            knn_clf = pickle.load(f)

    X_img = face_recognition.load_image_file(X_img_path)
    X_face_locations = face_recognition.face_locations(X_img)

    if len(X_face_locations) == 0:
        return []

    faces_encodings = face_recognition.face_encodings(X_img, known_face_locations=X_face_locations)

    closest_distances = knn_clf.kneighbors(faces_encodings, n_neighbors=1)
    are_matches = [closest_distances[0][i][0] <= distance_threshold for i in range(len(X_face_locations))]

    return [pred if rec else "unknown" for pred, rec in zip(knn_clf.predict(faces_encodings), are_matches)]


def take_a_photo():
    """
    通过摄像头照一张照片
    :return: 照片路径
    """
    cap = cv2.VideoCapture(0)
    start = time.time()

    ret, frame = cap.read()
    while time.time() - start < 3:
        ret, frame = cap.read()

    pic_path = '{dataset_dir}/{filename}'.format(dataset_dir=dataset_dir, filename=pic_filename)
    cv2.imwrite(pic_path, frame)

    cap.release()
    cv2.destroyAllWindows()

    return pic_path


def recognize():
    """

    :return: 人脸对应的用户名，默认返回unknown
    """
    # TODO: 人脸识别
    start = time.time()
    pic_path = take_a_photo()

    print("Take a photo with {} s".format(time.time() - start))
    start = time.time()

    predictions = predict(pic_path, model_path=model_path)
    print("Predict with {} s".format(time.time() - start))
    if len(predictions) == 0:
        print("Can't recognize the face!")
    elif len(predictions) > 1:
        print("Please others wait a moment!")
    else:
        return predictions[0]


def login():
    """

    :return: 用户名
    """
    username = recognize()
    return username
