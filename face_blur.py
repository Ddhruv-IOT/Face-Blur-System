# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 19:34:40 2021

@author: ACER
"""

import cv2

stream = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while 1:

    ret, frame = stream.read()
    cv2.imshow('Original Video', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.4, 4)

    for x, y, w, h in faces:                                       # to mask multiple faces at once
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)     # to make a rectangel on face
        blur = cv2.blur(frame[y:y+h, x:x+w], (50, 50))             # blur the face
        frame[y:y+h, x:x+w] = blur                                 # adding the blur part
        cv2.imshow('Blur Video', frame)                            # display the output

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()
