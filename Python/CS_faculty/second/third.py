"""Отфильтровать набор линий вида ax + by + c = 0 следующим образом:
из каждого параллельного подмножества линий данного набора оставить одну единственную линию – самую верхнюю
(а в случае линий, параллельных OY, – самую правую)"""

import math


def distance_to_nil(A, B, C):
    """функция для нахождения расстояния до точки от начала координат"""
    return abs(C / math.sqrt(A ** 2 + B ** 2))


def angle_koef(A, B):
    """функция возвращающая угловой коэффициент"""
    return -(A/B)


def answer_3(FILE_NAME):
    temp_dict = dict()

    with open(FILE_NAME) as f:
        # c помощью контекстного менеджера открываем файл для чтения строк
        line = f.readlines()

        for elem in line:
            # в каждой строке обрабатываем элемент и достаем оттуда коэффициенты
            elem = elem.split(" ")
            A, B, C = int(elem[0]), int(elem[1]), int(elem[2])
            koef = angle_koef(A, B)

            # добавляем угловой коэффициент в массив по ключу в словаре
            if koef in temp_dict:
                temp_dict[koef].append(distance_to_nil(A, B, C))
            else:
                temp_dict[koef] = [distance_to_nil(A, B, C)]

    # выбираем максимальное значение по ключу из всех и оставляем его
    for elem in temp_dict:
        temp_dict[elem] = max(temp_dict[elem])

    return temp_dict # возвращаем результат


print(answer_3("data.txt"))
