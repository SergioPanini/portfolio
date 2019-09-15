# Helper functions
import cv2
import os
import glob  # library for loading images from a directory
import numpy as np


# This function loads in images and their labels and places them in a list
# The list contains all images and their associated labels
# For example, after data is loaded, im_list[0][:] will be the first image-label pair in the list
def load_dataset(image_dir, type_name):
    # Populate this empty image list
    im_list = []
    image_types = [type_name]

    # Iterate through each color folder
    for im_type in image_types:

        # Iterate through each image file in each image_type folder
        # glob reads in any image with the extension "image_dir/im_type/*"
        for file in glob.glob(os.path.join(image_dir, im_type, "*")):

            # Read in the image
            # im = mpimg.imread(file)
            im = cv2.imread(file)

            # Check if the image exists/if it's been correctly read-in
            if not im is None:
                # Append the image, and it's type ("none", "pedistrain", "no_drive","stop","way-out","no_entry","road_works","parking","a_unevenness") to the image list
                im_list.append(im)

    return im_list

def edit_img(img):
	mask_list = []
	#маска цветов hsv
	ilowH = 0
	ihighH = 8
	ilowS = 23
	ihighS = 255
	ilowV = 25
	ihighV = 255

	ilowH1 = 169
	ihighH1 = 359
	ilowS1 = 14
	ihighS1 = 255
	ilowV1 = 25
	ihighV1 = 255

	ilowH2 = 100
	ihighH2 = 142
	ilowS2 = 108
	ihighS2 = 255
	ilowV2 = 25
	ihighV2 = 255

	#изменение размера
	img = cv2.resize(img, (64,64))

	img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	lower_hsv = np.array([ilowH, ilowS, ilowV])
	higher_hsv = np.array([ihighH, ihighS, ihighV])
	lower_hsv1 = np.array([ilowH1, ilowS1, ilowV1])
	higher_hsv1 = np.array([ihighH1, ihighS1, ihighV1])
	lower_hsv2 = np.array([ilowH2, ilowS2, ilowV2])
	higher_hsv2 = np.array([ihighH2, ihighS2, ihighV2])


	#бинаризация изображения по маскам
	mask = cv2.inRange(img, lower_hsv, higher_hsv)
	mask1 = cv2.inRange(img, lower_hsv1, higher_hsv1)
	mask2 = cv2.inRange(img, lower_hsv2, higher_hsv2)

	mask = cv2.erode(mask, (3,3), iterations = 2)
	mask = cv2.dilate(mask, (3,3), iterations = 4)
	mask1 = cv2.erode(mask1, (3,3), iterations = 2)
	mask1 = cv2.dilate(mask1, (3,3), iterations = 4)
	mask2 = cv2.erode(mask2, (3,3), iterations = 2)
	mask2 = cv2.dilate(mask2, (3,3), iterations = 4)

	mask_list.append((mask + mask1, mask2))
	return mask_list
	
type_name = 'way_out'
etalon_name = 'road_works_Black.png'
etalon_img = cv2.imread(etalon_name)
etalon_img = cv2.inRange(etalon_img, (0,0,0), (255,255,255))
imgs_list =  load_dataset("data/training/", type_name)
#for i in range(48):
	#print(i)
	#etalon_imgRed = abs(edit_img(imgs_list[i])[0][0] + edit_img(imgs_list[i + 1])[0][0])
	#etalon_imgBlue = abs(edit_img(imgs_list[i])[0][1] + edit_img(imgs_list[i + 1])[0][1])
for i in range(2443):
	imgs_list[i] = edit_img(imgs_list[i])[0][0]


s = 0
for n in range(2433):
	#s = sum(abs(imgs_list[n] - etalon_img))
	#print(s)



	for i in range(64):
		for j in range(64):
			if imgs_list[n][i][j] == etalon_img[i][j]:
				s += 1
print(s/n)
while True:
	#cv2.imshow('img', etalon_imgRed)
	#cv2.imshow('img', etalon_imgBlue)
	etalon_img = cv2.imread(etalon_name)
	cv2.imshow('Etal', etalon_img)
	cv2.imshow('img', imgs_list[n])

	if cv2.waitKey(1) == ord('q'):
		break

#cv2.imwrite(type_name + '_BlackRad.png', etalon_imgRad)
#cv2.imwrite(type_name + '_BlackBlue.png', etalon_imgBlue)

cv2.destroyAllWindows()