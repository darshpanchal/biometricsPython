import os, time
import cPickle
import numpy as np
import cv2
import warnings
warnings.filterwarnings("ignore")
from test_speaker import recog_speaker
from facerecog import face_recog

init = raw_input("Type Yes to carry on: ")

if init == "Yes" or init == "Y":
    name = raw_input("Enter Name: ")
    person = recog_speaker()
    print person
    if name == person:
        test_img1 = cv2.imread("test-data/" + name + ".jpg")
        image, label = face_recog(test_img1)
        if person == label:
            print "Door Unlocked"
        else:
            print "Authentication failed"
    else:
        print "Authentication failed"
        
