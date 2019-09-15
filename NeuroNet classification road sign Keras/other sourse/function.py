import cv2 as cv
import numpy as np

'''
тут кусок с бинаризацией, переменные с эталонами:

	по синему
	a_unevenness-bu = .... #a - sam etalon, ar - kol-vo odinakovih pixeley
	no_drive-bu = .... #b
	no_entry-bu = .... #c
	parking-bu = .... #d
	pedistrain-bu = .... #e
	road_works-bu = .... #f
	stop-bu = .... #g
	way_out-bu = .... #h

	по красному1
	a_unevenness-rd1 = .... #a - sam etalon, ar - kol-vo odinakovih pixeley
	no_drive-rd1 = .... #b
	no_entry-rd1 = .... #c
	parking-rd1 = .... #d
	pedistrain-rd1 = .... #e
	road_works-rd1 = .... #f
	stop-rd1 = .... #g
	way_out-rd1 = .... #h


	по красному2
	a_unevenness-rd2 = .... #a - sam etalon, ar - kol-vo odinakovih pixeley
	no_drive-rd2 = .... #b
	no_entry-rd2 = .... #c
	parking-rd2 = .... #d
	pedistrain-rd2 = .... #e
	road_works-rd2 = .... #f
	stop-rd2 = .... #g
	way_out-rd2 = .... #h

	по черному
	a_unevenness-bk = .... #a - sam etalon, ar - kol-vo odinakovih pixeley
	no_drive-bk = .... #b
	no_entry-bk = .... #c
	parking-bk = .... #d
	pedistrain-bk = .... #e
	road_works-bk = .... #f
	stop-bk = .... #g
	way_out-bk = .... #h

	КАРТИНКА, КОТОРУЮ РАСПОЗНАЕМ И ЕЁ ОБРАБОТКА
	picture-bu = ....
	picture-rd1 = ....
	picture-rd2 = ....
	picture-bk = ....


'''
#################################
def result(a, b, c, d, e, f, g, h, picture):
	ar=0
	br=0
	cr=0
	dr=0
	er=0
	fr=0
	gr=0
	hr=0

	for i in range(len(x))
	   for j in range(len(y))
	        if a[i][j]== picture[i][j]
	             ar+=1
			if b[i][j]==picture[i][j]
	             br+=1

	if ar>br:
	     pr1 = a
	     pr1r = ar
	else:
	     pr1 = b
	     pr1r = br

#######
	 for i in range(len(x))
	   for j in range(len(y))
	        if c[i][j]== picture[i][j]
	             cr+=1
			if d[i][j]==picture[i][j]
	             dr+=1

	if cr>dr:
	     pr2 = c
	     pr2r = cr
	else:
	     pr2 = d
	     pr2r = cr
########
	 for i in range(len(x))
	   for j in range(len(y))
	        if e[i][j]== picture[i][j]
	             er+=1
			if f[i][j]==picture[i][j]
	             fr+=1

	if er>fr:
	     pr3 = e
	     pr3r = er
	else:
	     pr3 = f
	     pr3r = fr
#######
	 for i in range(len(x))
	   for j in range(len(y))
	        if g[i][j]== picture[i][j]
	             gr+=1
			if h[i][j]==picture[i][j]
	             hr+=1

	if gr>hr:
	     pr4 = g
	     pr4r = gr
	else:
	     pr4 = h
	     pr4r = hr
#####
	if pr1r>pr2r:
	     pr11 = pr1
	     pr11r = pr1r
	else:
	     pr11 = pr2
	     pr11r = pr2r
#####
	if pr3r>pr4r:
	     pr12 = pr3
	     pr12r = pr3r
	else:
	     pr12 = pr4
	   	 pr12r = pr4r
#####
	if pr12r>pr11r:
	     res = pr12
	     resr = pr12r
	else:
	     res = pr11
	     resr = pr11r

	return res, resr
###########################################

res-bu, res-bu-r = result(a_unevenness-bu, no_drive-bu, no_entry-bu, parking-bu, pedistrain-bu, road_works-bu, stop-bu, way_out-bu, picture-bu)
res-rd1, res-rd1-r = result(a_unevenness-rd1, no_drive-rd1, no_entry-rd1, parking-rd1, pedistrain-rd1, road_works-rd1, stop-rd1, way_out-rd1, picture-rd1)
res-rd2, res-rd2-r = result(a_unevenness-rd2, no_drive-rd2, no_entry-rd2, parking-rd2, pedistrain-rd2, road_works-rd2, stop-rd2, way_out-rd2, picture-rd2)
res-bk, res-bk-r = result(a_unevenness-bk, no_drive-bk, no_entry-bk, parking-bk, pedistrain-bk, road_works-bk, stop-bk, way_out-bk, picture-bk)

