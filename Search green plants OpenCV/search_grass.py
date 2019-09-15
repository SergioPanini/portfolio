import cv2
import numpy as np

url = 'main.jpg' #url video

cap = cv2.VideoCapture(0)
img = cv2.imread(url)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_bin = cv2.inRange(img_hsv, (28,0,0), (100,255,255))
#cv2.blur(img_bin, (5,5))
cv2.erode(img_bin, (3,3), iterations = 4)
cv2.dilate(img_bin, (3,3), iterations= 4)


while True:
	_, frame = cap.read()
	#draw windows
	cv2.imshow('frame', frame)
	cv2.imshow('img', img)
	cv2.imshow('img_hsv', img_hsv)
	cv2.imshow('img_bin', img_bin)

	#get countours
	conturs = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	conturs = conturs[1]
	if conturs:
		conturs = sorted(conturs, key = cv2.contourArea, reverse = True)
		cv2.drawContours(img, conturs, -1, (255,0,255), 3)
		cv2.imshow('frameCon', img)
		#
		(x, y, w, h) = cv2.boundingRect(conturs[5])
		roimg = img[y:y+h, x:x+w]
		cv2.imshow('roimg', roimg )

	if cv2.waitKey(30) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()


