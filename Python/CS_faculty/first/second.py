"""2.Создать новый двумерный массив, исключив из переданного массива совпадающие столбцы.
(Совпадающие столбцы – столбцы, у которых все соответствующие элементы равны друз другу).
При формировании нового массива оставить только первый из каждого набора совпадающих столбцов."""
from itertools import zip_longest

matrix = [
    [0, 3, 4, 5, 4, 5, 4],
    [4, 3, 4, 5, 4, 5, 35],
    [5, 3, 4, 5, 4, 5, 34],
    [1, 3, 4, 5, 4, 5, 4]
]


def answer_2(array) -> list:

    transposed = list(zip(*array))
    temp = list()
    for elem in transposed:
        if elem not in temp:
            temp.append(elem)
    return list(zip(*temp))
    # print(list([x for x in y if x is not None] for y in zip_longest(*temp)))


print(answer_2(matrix))