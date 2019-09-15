# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cv2
import numpy as np

def callback(x):
    pass

#cap = cv2.VideoCapture('1')
#cv2.namedWindow('image')
#cv2.namedWindow('image1')

ilowH = 0
ihighH = 8
ilowS = 60
ihighS = 255
ilowV = 25
ihighV = 255

ilowH1 = 0
ihighH1 = 0
ilowS1 = 14
ihighS1 = 255
ilowV1 = 25
ihighV1 = 255
# create trackbars for color change
'''
cv2.createTrackbar('lowH', 'image', ilowH, 359, callback)
cv2.createTrackbar('highH', 'image', ihighH, 359, callback)

cv2.createTrackbar('lowS', 'image', ilowS, 255, callback)
cv2.createTrackbar('highS', 'image', ihighS, 255, callback)

cv2.createTrackbar('lowV', 'image', ilowV, 255, callback)
cv2.createTrackbar('highV', 'image', ihighV, 255, callback)

cv2.createTrackbar('lowH1', 'image1', ilowH1, 359, callback)
cv2.createTrackbar('highH1', 'image1', ihighH1, 359, callback)

cv2.createTrackbar('lowS1', 'image1', ilowS1, 255, callback)
cv2.createTrackbar('highS1', 'image1', ihighS1, 255, callback)

cv2.createTrackbar('lowV1', 'image1', ilowV1, 255, callback)
cv2.createTrackbar('highV1', 'image1', ihighV1, 255, callback)
'''
url1 = 'hsv.png'
while True:
    frame = cv2.imread(url1)
    frame = cv2.resize(frame, (64,64))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    key = cv2.waitKey(1)
    if  key == ord('w'):
        ilowH = ilowH + 1
    elif key == ord('s'):
        ihighH = ihighH - 1
    elif key == ord('e'):
        ilowS = ilowS + 1
    elif key == ord('d'):
        ihighS = ihighS - 1
    elif key == ord('r'):
        ilowV = ilowV + 1
    elif key == ord('f'):
        ihighV = ihighV - 1

    lower_hsv = np.array([ilowH, ilowS, ilowV])
    higher_hsv = np.array([ihighH, ihighS, ihighV])
    lower_hsv1 = np.array([ilowH1, ilowS1, ilowV1])
    higher_hsv1 = np.array([ihighH1, ihighS1, ihighV1])

    '''# grab the frame
    
    
    cv2.imshow('frame', frame)

    # get trackbar positions
    ilowH = cv2.getTrackbarPos('lowH', 'image')
    ihighH = cv2.getTrackbarPos('highH', 'image')
    ilowS = cv2.getTrackbarPos('lowS', 'image')
    ihighS = cv2.getTrackbarPos('highS', 'image')
    ilowV = cv2.getTrackbarPos('lowV', 'image')
    ihighV = cv2.getTrackbarPos('highV', 'image')

    ilowH1 = cv2.getTrackbarPos('lowH1', 'image1')
    ihighH1 = cv2.getTrackbarPos('highH1', 'image1')
    ilowS1 = cv2.getTrackbarPos('lowS1', 'image1')
    ihighS1 = cv2.getTrackbarPos('highS1', 'image1')
    ilowV1 = cv2.getTrackbarPos('lowV1', 'image1')
    ihighV1 = cv2.getTrackbarPos('highV1', 'image1')
    
    

    

    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
    mask1 = cv2.inRange(hsv, lower_hsv1, higher_hsv1)
    #frame = cv2.inRange(frame, lower_hsv, higher_hsv)
    # frame = cv2.bitwise_and(frame, frame, mask=mask)
    mask = cv2.erode(mask, (3,3), iterations = 2)
    mask = cv2.dilate(mask, (3,3), iterations = 4)
    mask1 = cv2.erode(mask1, (3,3), iterations = 2)
    mask1 = cv2.dilate(mask1, (3,3), iterations = 4)
    # show thresholded image
    cv2.imshow('win', mask)
    cv2.imshow('red', mask1)
    fr = mask + mask1
    cv2.imshow('mult', fr)'''

    if key == ord('q'):
        break
#cv2.imwrite('black_img.png', fr)
cv2.destroyAllWindows()
#cap.release()