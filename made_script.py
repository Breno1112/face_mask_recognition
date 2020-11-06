import numpy as np
import cv2
import random
from os import listdir

# face_cascade = cv2.CascadeClassifier('opencv-files/haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('opencv-files/haarcascade_eye.xml')
# mouth_cascade = cv2.CascadeClassifier('opencv-files/haarcascade_mcs_mouth.xml')
mask_cascade = cv2.CascadeClassifier('opencv-files/mask_cascade.xml')

CONST_FACE_NOT_FOUND = "ROSTO NAO ENCONTRADO"
CONST_WITHOUT_MASK = "SEM MASCARA"
CONST_WITH_MASK = "COM MASCARA"



# Adjust threshold value in range 80 to 105 based on your light.
bw_threshold = 80

# User message
font = cv2.FONT_HERSHEY_SIMPLEX
org = (30, 30)
weared_mask_font_color = (255, 255, 255)
not_weared_mask_font_color = (0, 0, 255)
thickness = 2
font_scale = 1

def classify(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert image in black and white
    (thresh, black_and_white) = cv2.threshold(gray, bw_threshold, 255, cv2.THRESH_BINARY)

    # detect face
    # faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Face prediction for black and white
    # faces_bw = face_cascade.detectMultiScale(black_and_white, 1.1, 4)

    # Eye prediction
    # eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)

    # Eye prediction for black and white
    # eyes_bw = eye_cascade.detectMultiScale(black_and_white, 1.1, 4)

    # Mouth prediction
    # mouth_rects = mouth_cascade.detectMultiScale(gray, 1.5, 5)

    # Mouth prediction black and white
    # mouth_rects_bw = mouth_cascade.detectMultiScale(black_and_white, 1.5, 5)

    # Mask prediction
    mask_rects = mask_cascade.detectMultiScale(gray, 1.5, 5)

    # Mask prediction black and white
    mask_rects_bw = mask_cascade.detectMultiScale(black_and_white, 1.5, 5)

    print("mask_rects: {}".format(mask_rects))
    print("mask_rects_bw: {}".format(mask_rects_bw))

    if len(mask_rects) > 0 or len(mask_rects_bw) > 0:
        if len(mask_rects) > 0:
            (x, y, w, h) = mask_rects[0]
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        elif len(mask_rects_bw) > 0:
            (x, y, w, h) = mask_rects_bw[0]
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        return CONST_WITH_MASK
    else:
        return CONST_WITHOUT_MASK

    # if len(eyes) == 0 and len(eyes_bw) == 0 and len(faces) == 0 and len(faces_bw) == 0:
    #     return CONST_FACE_NOT_FOUND
    # elif len(eyes) > 0 or len(eyes_bw) > 0:
    #     if len(mouth_rects) > 0 or len(mouth_rects_bw) > 0:
    #         return CONST_WITHOUT_MASK
    #     else:
    #         return CONST_WITH_MASK
    # elif len(faces) > 0 or len(faces_bw) > 0:
    #     return CONST_WITHOUT_MASK
    # else:
    #     return CONST_FACE_NOT_FOUND

def detectSingleImage(imgPath):
    img = cv2.imread(imgPath)
    response = classify(img)
    cv2.putText(img, response, org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
    cv2.imshow('Mask Detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detectVideo():
    # Read video
    cap = cv2.VideoCapture(0)

    while 1:
        # Get individual frame
        ret, img = cap.read()
        img = cv2.flip(img,1)

        classification = classify(img)
        cv2.putText(img, classification, org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
        cv2.imshow('video', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

def getAccuracy():
    with_mask_count = len(listdir("test-data/with_mask"))
    without_mask_count = len(listdir("test-data/without_mask"))
    with_mask = []
    without_mask = []
    print(with_mask_count)
    print(without_mask_count)
    for imagePath in listdir("test-data/with_mask"):
        response = classify(cv2.imread("test-data/with_mask/{}".format(imagePath)))
        print("{}: {}".format(imagePath, response))
        if response == CONST_WITH_MASK:
            with_mask.append(imagePath)
    for imagePath in listdir("test-data/without_mask"):
        response = classify(cv2.imread("test-data/without_mask/{}".format(imagePath)))
        print("{}: {}".format(imagePath, response))
        if response == CONST_WITHOUT_MASK:
            without_mask.append(imagePath)
    print(with_mask)
    print(without_mask)
    accuracy = ((len(without_mask)/without_mask_count) + (len(with_mask)/with_mask_count))/0.02
    print("Acurácia: {:.2f}%".format(accuracy))

detectSingleImage("test-data/with_mask/francisquinho.png")
# detectVideo()
# getAccuracy()
