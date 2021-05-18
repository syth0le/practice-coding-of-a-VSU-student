"""3.Для набора точек на плоскости найти такие три точки,
 для которых периметр треугольника с вершинами в данных точках будет минимальным.
  В случае существования нескольких подходящих троек точек – выбрать произвольную."""
import math

dots = [(1, -3), (2, 4), (3, -6), (-5, -1), (-5, -3)]

def answer_3(dots):

    AB = math.sqrt(math.pow(angle2.getX() - angle1.getX(), 2) + math.pow(angle2.getY() - angle1.getY(), 2));
    AC = math.sqrt(math.pow(angle3.getX() - angle1.getX(), 2) + math.pow(angle3.getY() - angle1.getY(), 2));
    BC = math.sqrt(math.pow(angle3.getX() - angle2.getX(), 2) + math.pow(angle3.getY() - angle2.getY(), 2));
    return AB + AC + BC

