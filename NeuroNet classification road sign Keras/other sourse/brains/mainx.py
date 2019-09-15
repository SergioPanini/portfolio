import helpers
import cv2
import random
import numpy as np


a=cv2.imread("1e.jpg")
b=cv2.imread("2e.jpg")
c=cv2.imread("3e.jpg")
d=cv2.imread("4e.jpg")
e=cv2.imread("5e.jpg")
f=cv2.imread("6e.jpg")
g=cv2.imread("7e.jpg")
h=cv2.imread("8e.jpg")
# Загрузка данных из учебных, проверочных и валидационных данных
def load_data():
    """ Формирование обучающего, тренировочного и тестового массива изображений.
    Вспомогательный файл helpers.py формирует массив изображений по заданному пути.

    Выходные данные:
    IMAGE_LIST - массив тренировочных изображений
    TEST_IMAGE_LIST - массив тестовых изображений
    VALIDATION_IMAGE_LIST - массив валидационных изображений (по этому массиву осуществляется
    проверка работы алгоритма
    """

    IMAGE_DIR_TRAINING = "data/training/"
    IMAGE_DIR_TEST = "data/test/"
    IMAGE_DIR_VALIDATION = "data/val/"
    IMAGE_LIST = helpers.load_dataset(IMAGE_DIR_TRAINING)
    TEST_IMAGE_LIST = helpers.load_dataset(IMAGE_DIR_TEST)
    VALIDATION_IMAGE_LIST = helpers.load_dataset(IMAGE_DIR_VALIDATION)

    return IMAGE_LIST, TEST_IMAGE_LIST, VALIDATION_IMAGE_LIST


# приведение входного изображения к стандартному виду
def standardize_input(image):
    """Приведение изображений к стандартному виду. Если вы хотите преобразовать изображение в
    формат, одинаковый для всех изображений, сделайте это здесь. В примере представлено приведение размера к одинаковому для каждого изображения

    Входные данные: изображение

    Выходные данные: стандартизированное изображений.
    """
    hsv_min = np.array((142,63,48), np.uint8)
    hsv_max = np.array((0,0,88), np.uint8)

    while(True):
      

        # to hsv
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV )
        masc = cv2.inRange(hsv, hsv_min, hsv_max)

        # binariation
        # masc = cv.inRange(frame_modified, (51,86,1), (119,175,255))
        # make blur
        masc = cv2.erode(masc, None, iterations = 2)
        masc = cv2.dilate(masc, None, iterations = 4)
        # countour
        conture = cv2.findContours(masc, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        conture = conture[1]
        
        if conture:
            conture = sorted(conture, key = cv2.contourArea, reverse = True)
            # cv.drawContours(frame, conture, -1, (255,0,0), 3)
            
            # make rectangular from free counour
            (x,y,w,h) = cv2.boundingRect(conture[0])
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)

            # crop
            image = image[y:y+h, x:x+w]
            # change size
            #image = cv.resize(image,(64,64))
            
            # show
            #cv.imshow("Frame", framecropted)

            # cv.imshow("croped",cropedFrame)


        cv2.imshow("Frame modified", masc)

    ## TODO: Выполните необходимые преобразования изображения для стандартизации, если это необходимо (обрезка, поворот, изменение размера)
    standard_im = np.copy(image)

    standard_im = cv2.resize(standard_im, (64, 64))
    return standard_im


# Перекодировка из текстового названия в массив данных
def one_hot_encode(label):
    """ Функция осуществляет перекодировку текстового входного сигнала
     в массив элементов, соответствующий выходному сигналу

     Входные параметры: текстовая метка (прим.  pedistrain)

     Выходные параметры: метка ввиде массива
     """
    one_hot_encoded = []
    if label == "none":
        one_hot_encoded =  [0, 0, 0, 0, 0, 0, 0, 0]
    elif label == "pedistrain":
        one_hot_encoded = [1, 0, 0, 0, 0, 0, 0, 0]
    elif label == "no_drive":
        one_hot_encoded = [0, 1, 0, 0, 0, 0, 0, 0]
    elif label == "stop":
        one_hot_encoded = [0, 0, 1, 0, 0, 0, 0, 0]
    elif label == "way_out":
        one_hot_encoded = [0, 0, 0, 1, 0, 0, 0, 0]
    elif label == "no_entry":
        one_hot_encoded = [0, 0, 0, 0, 1, 0, 0, 0]
    elif label == "road_works":
        one_hot_encoded = [0, 0, 0, 0, 0, 1, 0, 0]
    elif label == "parking":
        one_hot_encoded = [0, 0, 0, 0, 0, 0, 1, 0]
    elif label == "a_unevenness":
        one_hot_encoded = [0, 0, 0, 0, 0, 0, 0, 1]

    return one_hot_encoded


# приведение всего набора изображений к стандартному виду
def standardize(image_list):
    """Функция осуществляет приведение всего набора изображений к стндартному виду

    Входные данные: блок изображений (массив)

    Выходные данные: стандартизированный блок изображений
    """

    standard_list = []

    for item in image_list:
        image = item[0]
        label = item[1]

        # стандартизация каждого изображения
        standardized_im = standardize_input(image)

        # перекодировка из названия в массив
        one_hot_label = one_hot_encode(label)

        # Append the image, and it's one hot encoded label to the full, processed list of image data
        standard_list.append((standardized_im, one_hot_label))

    return standard_list


# совокупность функций классификации
def predict_label(rgb_image):
    """ Необходимо реализовать самостоятельно.
    Функция, предназначенная для классификации изображения

    Входные данные: изображение

    Выходные данные: метка изображения
    """
    ## TODO: обьедините ваши функции классификации в одну программу или напишите код внутри этой функции
    ar=0
    br=0
    cr=0
    dr=0
    er=0
    fr=0
    gr=0
    hr=0

    for i in range(len(x)):
        for j in range(len(y)):
            if a[i][j]== picture[i][j]:
                 ar+=1
            if b[i][j]==picture[i][j]:
                 br+=1

    if ar>=br:
         pr1 = a
         pr1r = ar
    else:
         pr1 = b
         pr1r = br

#######
    for i in range(len(x)):
        for j in range(len(y)):
            if c[i][j]== picture[i][j]:
                 cr+=1
            if d[i][j]==picture[i][j]:
                 dr+=1

    if cr>=dr:
         pr2 = c
         pr2r = cr
    else:
         pr2 = d
         pr2r = cr
########
    for i in range(len(x)):
        for j in range(len(y)):
            if e[i][j]== picture[i][j]:
                 er+=1
            if f[i][j]==picture[i][j]:
                 fr+=1

    if er>=fr:
         pr3 = e
         pr3r = er
    else:
         pr3 = f
         pr3r = fr
#######
    for i in range(len(x)):
        for j in range(len(y)):
            if g[i][j]== picture[i][j]:
                 gr+=1
            if h[i][j]==picture[i][j]:
                 hr+=1

    if gr>=hr:
         pr4 = g
         pr4r = gr
    else:
         pr4 = h
         pr4r = hr
#####
    if pr1r>=pr2r:
         pr11 = pr1
         pr11r = pr1r
    else:
         pr11 = pr2
         pr11r = pr2r
#####
    if pr3r>=pr4r:
         pr12 = pr3
         pr12r = pr3r
    else:
         pr12 = pr4
         pr12r = pr4r
#####
    if pr12r>=pr11r:
         res = pr12
         resr = pr12r
    else:
         res = pr11
         resr = pr11r

    label = ""
    if res == a:
        label = "a_unevenness"
    elif res == b:
        label = "no_drive"
    elif res == c:
        label = "no_entry"
    elif res == d:
        label = "parking"
    elif res == e:
        label = "pedistrain"
    elif res == f:
        label = "road_works"
    elif res == g:
        label = "stop"
    elif lres == h:
        label = "way_out"

    if resr < 1229:
        label = "none"


    # Если вы получаете текстовые метки изображения, то используйте функцию:
    predicted_label = one_hot_encode(label)
    # чтобы преобразовать текстовую метку в массив.

    ##predicted_label = [1, 0, 0, 0, 0, 0, 0, 0] его вроде нельзя комментить, но я комменчу

    return predicted_label


# Получение списка неклассифицированных изображений
def get_misclassified_images(test_images):
    """Определение точности
    Сравните результаты вашего алгоритма классификации
    с истинными метками и определите точность.

    Входные данные: массив с тестовыми изображениями
    Выходные данные: массив с неправильно классифицированными метками

    Этот код используется для тестирования и не должен изменяться
    """
    misclassified_images_labels = []
    # Классификация каждого изображения и сравенение с реальной меткой
    for image in test_images:
        # получение изображения и метки
        im = image[0]
        true_label = image[1]
        # метки должны быть в виде массива
        assert (len(true_label) == 8), "Метка имеет не верную длинну (8 значений)"

        # Получение метки из написанного Вами классификатора
        predicted_label = predict_label(im)
        assert (len(predicted_label) == 8), "Метка имеет не верную длинну (8 значений)"

        # Сравнение реальной и предсказанной метки
        if (predicted_label != true_label):
            # Если значения меток не совпадают, то изображение помечается как неклассифицированное
            misclassified_images_labels.append((im, predicted_label, true_label))

    # Возвращение неклассифицированных изображений [image, predicted_label, true_label] values
    return misclassified_images_labels


def main():
    ## загрузка учебных изображений
    IMAGE_LIST, TEST_IMAGE_LIST, VALIDATION_IMAGE_LIST = load_data()
    ## Отображение изображения, приведенного к стандартному виду (размер 32х32) и его метки (массива чисел)
    STANDARDIZED_LIST = standardize(IMAGE_LIST)
    STANDARDIZED_TEST_LIST = standardize(TEST_IMAGE_LIST)
    random.shuffle(STANDARDIZED_TEST_LIST)

    # [1]
    ## Пример работы с изображением из списка тренировочных изображений

    # Получим изображение и его метку
    standart_image = STANDARDIZED_LIST[1520][0]
    standart_image_label = STANDARDIZED_LIST[1520][1]
    #
    predict_image_label = predict_label(standart_image)

    print("Реальный класс изображения: {} Предсказанный класс изображения {}".format(standart_image_label,
                                                                                     predict_image_label))
    # Чтобы отобразить изображение раскомментируйте 2 строки ниже:
    # cv2.imshow("standart_test_im", standart_image)
    # cv2.waitKey(0)

    # [2]
    ## сравнение учебных и тестовых изображений
    # поиск неклассифицированных изображений в тестовой выборке
    MISCLASSIFIED = get_misclassified_images(STANDARDIZED_TEST_LIST)
    # Вы также можете увидеть изображения, которые не удалось классифицировать раскомментировав 2 строчки ниже:
    # cv2.imshow("MISCLASSIFIED", MISCLASSIFIED[10][0])
    # cv2.waitKey(0)

    # вычисление точности
    total = len(STANDARDIZED_TEST_LIST)
    num_correct = total - len(MISCLASSIFIED)
    accuracy = num_correct / total

    print('Точность: ' + str(accuracy))
    print("Число не распознанных изображений = " + str(len(MISCLASSIFIED)) + ' из ' + str(total))


if __name__ == '__main__':
    main()
