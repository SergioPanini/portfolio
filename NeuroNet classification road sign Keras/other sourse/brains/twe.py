import cv2
import numpy as np
import glob
import os

type_list = [ "pedistrain", "no_drive","stop","way_out","no_entry","road_works","parking","a_unevenness"]
Etalon_img = []
for i in type_list:
	url = i + '.png'
	img = cv2.imread(url)
	
	print(img)
	#img = cv2.inRange(img, (250,250,250), (255,255,255))
