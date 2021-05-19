"""Отфильтровать набор линий вида ax + by + c = 0 следующим образом:
из каждого параллельного подмножества линий данного набора оставить одну единственную линию – самую верхнюю
(а в случае линий, параллельных OY, – самую правую)"""

import math


def distance_to_nil(A, B, C):
    return abs(C / math.sqrt(A ** 2 + B ** 2))


def angle_koef(A, B):
    return -(A/B)


def answer_3(FILE_NAME):
    temp_dict = dict()

    with open(FILE_NAME) as f:
        line = f.readlines()

        for elem in line:
            elem = elem.split(" ")
            A, B, C = int(elem[0]), int(elem[1]), int(elem[2])
            koef = angle_koef(A, B)
            if koef in temp_dict:
                temp_dict[koef].append(distance_to_nil(A, B, C))
            else:
                temp_dict[koef] = [distance_to_nil(A, B, C)]

    for elem in temp_dict:
        temp_dict[elem] = max(temp_dict[elem])

    return temp_dict


print(answer_3("data.txt"))
