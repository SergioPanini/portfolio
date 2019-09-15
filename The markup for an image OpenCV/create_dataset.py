import cv2 as cv
import numpy as np
#url = 'D:\\Documents\\python\\hackaton31aug\\Video.mp4'
cap = cv.VideoCapture(0)
cv.namedWindow('frame')

def get_point(event, x, y, flags, params):
	global point
	if event == cv.EVENT_LBUTTONDOWN:
		point = (x, y)
		print(point)
point = ()
cv.setMouseCallback('frame', get_point)
id_frame = 0
r = 4

while True:
	_, frame = cap.read()
	cv.resize(frame, (480, 640))
	if id_frame // 10 == 0:
		msk  = np.zeros((480,640,3), np.uint8)
		while True:
			cv.imshow('frame', frame)
			if point != ():
				for i in range(-r, r):
					for j in range(-r, r):
						msk[point[1] + i][point[0] + j] = (255, 255, 255)
			cv.imshow('msk', msk)
			if cv.waitKey(100) == ord('n'):
				print('writing img')
				cv.imwrite('C:/Users/Sergey/Desktop/optical_flow/GGGG/data_img' + str(id_frame) + '.jpg', frame)
				cv.imwrite('C:/Users/Sergey/Desktop/optical_flow/GGGG/data_mask'+ str(id_frame) + '.jpg', msk)
				point = ()
				break

#

	id_frame += 1
	if cv.waitKey(100) == ord('q'):
		break
cv.destroyAllWindows()
cap.release()