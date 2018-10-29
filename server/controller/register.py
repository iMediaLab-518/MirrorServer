import math
import pickle
import re
import shutil

from imutils.video import VideoStream
import imutils
import cv2
import os
import os.path
import time

from sklearn import neighbors
import face_recognition
from ..util import config
from ..models import User

cascade_path = config['global']['cascade']
dataset_dir = config['global']['dataset']
train_dir = os.path.join(dataset_dir, 'train')
model_dir = config['global']['model']
# 读取所有配置

VIDEO_TIME = 8  # VIDEO_TIME是之后的语音提示语的长度，会进行这么长时间的面部录入


def image_files_in_folder(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if re.match(r'.*\.(jpg|jpeg|png)', f, flags=re.I)]


def handle_pic(orig):
    """
    处理图片，修改图片分辨率并灰度化

    :param orig: 图片类
    :return: 处理之后的图片
    """
    orig = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
    orig = cv2.resize(orig, (320, 240), interpolation=cv2.INTER_AREA)
    return orig


def train(train_dir, model_save_path=None, n_neighbors=None, knn_algo='ball_tree'):
    """
    对train_dir文件夹下的所有图片进行训练，文件夹名称就是这个模型的名称

    :param train_dir: 需要训练的图片的文件夹
    :param model_save_path: 模型保存的地址
    :param n_neighbors: kNN的k
    :param knn_algo: 默认kNN算法
    :return: 训练模型
    """
    X = []
    y = []

    for img_path in image_files_in_folder(train_dir):
        image = face_recognition.load_image_file(img_path)
        face_bounding_boxes = face_recognition.face_locations(image)

        if len(face_bounding_boxes) == 1:
            X.append(face_recognition.face_encodings(image, known_face_locations=face_bounding_boxes)[0])
            y.append(train_dir.split('/')[1])

    if n_neighbors is None:
        n_neighbors = int(round(math.sqrt(len(X))))

    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=knn_algo, weights='distance')
    knn_clf.fit(X, y)

    if not os.path.exists(model_dir):
        os.mkdir(model_dir)

    if model_save_path is not None:
        with open(model_save_path, 'wb') as f:
            pickle.dump(knn_clf, f)
            # 使用pickle持久化模型

    return knn_clf


def register(person):
    """
    开始录入人脸，保存在person文件夹下
    :param person: 人物名称
    """
    if not os.path.exists(train_dir):
        os.mkdir(train_dir)

    person_dir = '{train_dir}/tmp'.format(train_dir=train_dir)
    if not os.path.exists(person_dir):
        os.mkdir(person_dir)
    # 图片保存的路径

    total = len(os.listdir(person_dir))
    current = 0

    start = time.time()
    detector = cv2.CascadeClassifier(cascade_path)
    vs = VideoStream(src=0).start()

    print("Initlize the camera with {} s".format(time.time() - start))
    start = time.time()

    while current < 5:
        if time.time() - start >= VIDEO_TIME:
            break
        frame = vs.read()
        orig = frame.copy()
        frame = imutils.resize(frame, width=400)

        rects = detector.detectMultiScale(
            cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.1,
            minNeighbors=5, minSize=(30, 30))
        # 拍摄的图片的人脸数量

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
        time.sleep(1.5)

    if not os.path.exists(train_dir):
        os.mkdir(train_dir)

    start = time.time()
    print("[INFO] Start training the pictures!")
    # train(person_dir, model_save_path=os.path.join(model_dir, "{}.clf".format(person)), n_neighbors=2)
    model_count = User.query.count() + 1
    train(person_dir, model_save_path=os.path.join(model_dir, "{}.clf".format(model_count)), n_neighbors=2)

    print("[INFO] Train complete with {} s".format(time.time() - start))

    shutil.rmtree(person_dir)  # 递归删除文件夹

    cv2.destroyAllWindows()
    vs.stop()
