import cv2
import time
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

dataset_dir = config['global']['dataset']
pic_filename = 'unknown.png'


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
    return 'unknown'


def login():
    """

    :return: 用户名
    """
    username = recognize()
    return username
