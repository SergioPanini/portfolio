import cv2 as cv
import helpers
#cap = cv.VideoCapture('1.mp4')

#img_list[номер изображения с типом][0-img/1-type]
#imgs_list = helpers.load_dataset('data/test')
print(imgs_list[150][1])

while(True):
    #ret, frameSource = cap.read()
    italon_first = cv.imread('italon_first.jpg')
    italon_second= cv.imread('italon_second.jpg')
    frameSource = cv.imread('1q.jpg')
    
    #изменение исхоного "видеопотока"
    frameSource = cv.resize(frameSource, (256,256))
    italon_first = cv.resize(italon_first, (256,256))
    italon_second = cv.resize(italon_second, (256,256))
    cv.imshow('Frame New', frameSource)
    cv.imshow('italon_first', italon_first)
    cv.imshow('italon_second', italon_second)




    #бинаризация
    frameBin = cv.inRange(frameSource, (89,124,73), (255,255,255))
    italon_first = cv.inRange(italon_first, (89,124,73), (255,255,255))
    italon_second = cv.inRange(italon_second, (89,124,73), (255,255,255))

    cv.imshow('Bin', frameBin)

    #удаление ряби 
    frameBin = cv.erode(frameBin, (3,3), iterations = 2)
    frameBin = cv.dilate(frameBin, (3,3), iterations = 4)

    #получение контуров
    conturs = cv.findContours(frameBin, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    conturs = conturs[1]
    if conturs:
    	conturs = sorted(conturs, key = cv.contourArea, reverse = True)
    	cv.drawContours(frameSource, conturs, 0, (255,0,255), 3)
    	cv.imshow('frameCon', frameSource)

    #
    #cv.imshow('imgs', cv.resize(imgs_list[150][0], (256,256)))

    if cv.waitKey(1) == ord('q'):
        break

#cap.release()
cv.destroyAllWindows()