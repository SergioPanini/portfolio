# Helper functions
import cv2
import os
import glob  # library for loading images from a directory
import numpy as np

def one_hot_encode(label):
    """ Функция осуществляет перекодировку текстового входного сигнала
     в массив элементов, соответствующий выходному сигналу

     Входные параметры: текстовая метка (прим.  pedistrain)

     Выходные параметры: метка ввиде массива
     """
    if label == "none":
        one_hot_encoded = 0
    elif label == "pedistrain":
        one_hot_encoded = 1
    elif label == "no_drive":
        one_hot_encoded = 2
    elif label == "stop":
        one_hot_encoded = 3
    elif label == "way_out":
        one_hot_encoded = 4
    elif label == "no_entry":
        one_hot_encoded = 5
    elif label == "road_works":
        one_hot_encoded = 6
    elif label == "parking":
        one_hot_encoded = 7
    elif label == "a_unevenness":
        one_hot_encoded = 8

    return one_hot_encoded

# This function loads in images and their labels and places them in a list
# The list contains all images and their associated labels
# For example, after data is loaded, im_list[0][:] will be the first image-label pair in the list
def load_dataset(image_dir):
    # Populate this empty image list
    im_list = []
    out_list = []
    im_type_list = []
    image_types = ["none", "pedistrain", "no_drive","stop","way_out","no_entry","road_works","parking","a_unevenness"]

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
                im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                im = cv2.resize(im, (20,20))
                im_list.append(im)
                im_type_list.append(one_hot_encode(im_type))
    
    #print('im_type ', im_type_list)
    #print('im ', im_list)
    #im_list = np.array(im_list)
    #im_list.tolist()
    
    out_list.append(im_list)
    out_list.append(im_type_list)

    return out_list


a = load_dataset("data/test/")
#print(a[0])
print(a[1])
#print('im: ', len(a[0]))
#print('types', len(a[1]))

#new_list__ = []
#for i in range(len(a[0])):
#   new_list__.append(a[0][i])
#new_list__.append(a[0][253])
#new_list__.append(a[0][254])
#print('nw ', new_list__)
#print('new_list_im', a[0][253] / 255.0)


#ls2= np.array(a[0])
#ls2.tolist()
#print(ls2)