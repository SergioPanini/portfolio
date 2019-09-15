import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

def edit_img(img):
    
    lists = []
    
    ilowH = 0
    ihighH = 8
    ilowS = 23
    ihighS = 255
    ilowV = 25
    ihighV = 255


    low_hsv1 = np.array([ilowH, ilowS, ilowV])
    hig_hsv1 = np.array([ihighH, ihighS, ihighV])

    #изменение размера и цветового формата
    #img = cv.resize(img, (100,100))
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    
    #бинаризация изображения по маскам
    mask = cv.inRange(img_hsv, low_hsv1, hig_hsv1)
    
    #уменьшение шумов
    mask = cv.erode(mask, (3,3), iterations = 2)
    mask = cv.dilate(mask, (3,3), iterations = 4)
    
    lists.append(mask)
    lists.append(img_hsv)
    return lists


while True :
	ret, frameSource = cap.read()
	#frameSource = cv.resize(frameSource, (100,100))
	cv.imshow('Frame', frameSource)

	bin_hsv = edit_img(frameSource)
	
	cv.imshow('Frame_bin', bin_hsv[0])
	
	cv.imshow('Frame_hsv', bin_hsv[1])
	
	if cv.waitKey(1) == ord('q'):
		break

cap.release()
cv.destroyAllWindows()

cv.imwrite('hsv.png', bin_hsv[1])
cv.imwrite('bin.png', bin_hsv[0])