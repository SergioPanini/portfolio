import helpers
import cv2
import random
import numpy as np


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
    ## TODO: Выполните необходимые преобразования изображения для стандартизации, если это необходимо (обрезка, поворот, изменение размера)
    standard_im = np.copy(image)
    #my code

    standard_im = cv2.resize(standard_im, (64, 64))
    
    
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

    standard_im = edit_img(image)
    #my code
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
        one_hot_encoded = [0, 0, 0, 0, 0, 0, 0, 0]
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
    #my code

    
    #my code

    # Если вы получаете текстовые метки изображения, то используйте функцию:
    # predicted_label = one_hot_encode(label)
    # чтобы преобразовать текстовую метку в массив.

    predicted_label = [1, 0, 0, 0, 0, 0, 0, 0]

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
