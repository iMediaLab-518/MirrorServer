from imutils.video import VideoStream
import imutils
import time
import cv2
import os
import os.path
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

cascade_path = config['global']['cascade']
dataset_dir = config['global']['dataset']
VIDEO_TIME = 30  # time of audio


def register(person):
    person_dir = '{dataset_dir}/{person}'.format(dataset_dir=dataset_dir, person=person)
    if not os.path.exists(person_dir):
        os.mkdir(person_dir)

    total = len(os.listdir(person_dir))  # pics number existed

    detector = cv2.CascadeClassifier(cascade_path)
    vs = VideoStream(src=0).start()

    start = time.time()
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
            print("Forward")
            # TODO : Frontend
        elif cur_person_number > 1:
            print("Wait!")
            # TODO : Frontend
        else:
            p = os.path.sep.join([person_dir, "{}.png".format(str(total).zfill(5))])
            cv2.imwrite(p, orig)
            total += 1
            print("Successful! Current : {}".format(total))

        # cv2.imshow("Frame", frame)
        # key = cv2.waitKey(1) & 0xFF
        # Wait for press

    cv2.destroyAllWindows()
    vs.stop()
