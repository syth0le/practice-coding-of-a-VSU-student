"""3.Для набора точек на плоскости найти такие три точки,
 для которых периметр треугольника с вершинами в данных точках будет минимальным.
  В случае существования нескольких подходящих троек точек – выбрать произвольную."""
import math

dots = [((1, -3), (2, 4), (3, -6)),
        ((3, 3), (2, 4), (13, -16)),
        ((5, 0), (3, -6), (3, -6)),
        ((13, 7), (2, 4), (5, 0)),
        ((34, 35), (2, 9), (3, -6))]


def answer_3(dots):

    res = dict()

    for triangle in dots:

        x_1, y_1 = triangle[0]
        x_2, y_2 = triangle[1]
        x_3, y_3 = triangle[2]

        AB = math.sqrt(math.pow(x_2-x_1, 2) + math.pow(y_2-y_1, 2))
        AC = math.sqrt(math.pow(x_3-x_2, 2) + math.pow(y_3-y_2, 2))
        BC = math.sqrt(math.pow(x_1-x_3, 2) + math.pow(y_1-y_3, 2))

        perimeter = AB + AC + BC
        if perimeter not in res:
            res[perimeter] = triangle

    return res[min(res)]


print(answer_3(dots))
