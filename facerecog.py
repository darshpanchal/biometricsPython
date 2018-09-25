import cv2
import os
import numpy as np

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    if (len(faces) == 0):
        return None, None
    
    (x, y, w, h) = faces[0]
    
    return gray[y:y+w, x:x+h], faces[0]

def face_recog(test_img):
    subjects = ["", "tom", "modi"]
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('trained_data.yml')
    img = test_img
    face, rect = detect_face(test_img)
    label, confidence = face_recognizer.predict(face)
    label_text = subjects[label]
    #print label_text
    #draw_rectangle(img, rect)
    #draw_text(img, label_text, rect[0], rect[1]-5)
    return img, label_text