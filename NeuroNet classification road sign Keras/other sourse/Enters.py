import cv2
url1 = 'way_out_Black' + '.png'
url2 = 'way_out_BlackRad_test' + '.png'

#загрузка эталонных катинок
etalon_one = cv2.imread(url1)
etalon_one = cv2.inRange(etalon_one, (250,250,250), (255,255,255))

etalon_twe = cv2.imread(url2)
etalon_twe = cv2.inRange(etalon_twe, (250,250,250), (255,255,255))

etalon = etalon_one

#for x in range(64):
#	for y in range(64):
#		if etalon_one[x][y] != etalon_twe[x][y]:
#			etalon[x][y] = 0
etalon = etalon_one + etalon_twe

while True:
	cv2.imshow(url1, etalon_one)
	cv2.imshow(url2, etalon_twe)

	if cv2.waitKey(1) == ord('q'):
		break
cv2.destroyAllWindows()
cv2.imwrite('WWWW_8.png', etalon)