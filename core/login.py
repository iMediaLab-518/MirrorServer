import os
import pickle

import cv2
import time
import face_recognition

from utils.config import config

dataset_dir = config['global']['dataset']
model_dir = config['global']['model']
# 读取配置

pic_filename = 'unknown.png'
# 拍照和识别默认都使用这个文件名

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


# 图片扩展名

def single_predict(X_img_path, knn_clf=None, model_path=None, distance_threshold=0.4):
    """
    内存足够则直接将所有模型加载到内存中，识别每一个图片的时候直接从内存中调用模型，没有IO损耗。
    内存不足够这只能给出model_path增加IO操作减少内存损耗

    distance_threshold是最短距离参数，KNN算法要计算一个数据点和其他所有数据点的距离，距离大于一定程度则视为识别失败，即unknown

    :param X_img_path: 要预测的图片路径
    :param knn_clf: 人脸模型（使用KNN算法训练）
    :param model_path: 模型路径
    :param distance_threshold: 要识别的KNN算法中的最短距离
    :return:
    """
    if not os.path.isfile(X_img_path) or os.path.splitext(X_img_path)[1][1:] not in ALLOWED_EXTENSIONS:
        raise Exception("Invalid image path: {}".format(X_img_path))

    if knn_clf is None and model_path is None:
        raise Exception("Must supply knn classifier either thourgh knn_clf or model_path")

    if knn_clf is None:
        with open(model_path, 'rb') as f:
            knn_clf = pickle.load(f)
            # 模型是用pickle持久化的

    X_img = face_recognition.load_image_file(X_img_path)
    X_face_locations = face_recognition.face_locations(X_img)  # 加载每一张脸的位置

    if len(X_face_locations) == 0:
        return []

    faces_encodings = face_recognition.face_encodings(X_img, known_face_locations=X_face_locations)

    closest_distances = knn_clf.kneighbors(faces_encodings, n_neighbors=1)
    are_matches = [closest_distances[0][i][0] <= distance_threshold for i in
                   range(len(X_face_locations))]  # 提取所有计算距离小于distance_threshold的值得脸

    return [True if rec else "unknown" for rec in
            are_matches]  # 如果识别成功则返回识别出的名称，否则返回unknown


def predict(X_img_path, distance_threshold=0.4):
    """

    :param X_img_path: 要预测的图片路径
    :param distance_threshold: 要识别的KNN算法中的最短距离，越小越严格
    :return:
    """
    X_img = face_recognition.load_image_file(X_img_path)
    X_face_locations = face_recognition.face_locations(X_img)  # 加载每一张脸的位置
    # 检测脸的位置和对脸进行编码是耗时最长的

    if len(X_face_locations) == 0:
        return []
    faces_encodings = face_recognition.face_encodings(X_img, known_face_locations=X_face_locations)

    for model in os.listdir(model_dir):
        # 使用每一个模型对图片进行检测
        model_path = os.path.join(model_dir, model)
        name = model.split('.')[0]
        with open(model_path, 'rb') as f:
            clf = pickle.load(f)
            closest_distances = clf.kneighbors(faces_encodings, n_neighbors=1)
            are_match = closest_distances[0][0][0] <= distance_threshold

            if are_match:
                return name
    return "unknown"


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
        # 因为刚开启摄像头是不采光，所以直接拍摄会是一张黑色很模糊的图片，所以需要等待一段时间拍摄

    pic_path = '{dataset_dir}/{filename}'.format(dataset_dir=dataset_dir, filename=pic_filename)
    cv2.imwrite(pic_path, frame)

    cap.release()
    cv2.destroyAllWindows()

    return pic_path


def login():
    """

    :return: 用户名
    """
    pic_path = take_a_photo()
    username = predict(pic_path)
    return username
