"""Отсортировать заданный в произвольном порядке набор студентов
(каждый студент описывается в виде: ФИО, номер курса, номер группы)
сначала по номеру курса, затем по номеру группы, затем по ФИО."""

# данные вида: [[name:str, course: int, group: int]]
data = [("name_1", 2, 418), ("name_2", 1, 542), ("name_3", 4, 319), ("name_4", 3, 444)]


def student_sorting(data: list, on_sort: str = "name") -> list:
    """функция сортировки массива студентов
        принимает значения: - data вида list of lists. - on_sort: str параметр сортировки.
        name - Сортировка массива по ФИО
        course - сортировка массива по номеру курса
        group - сортировка массива по номеру группы
        """

    # сортируем по параметру и с помощью лямбда функции сортируем по индексу в массиве
    if on_sort == "name":
        data.sort(key=lambda val: val[0])
    elif on_sort == "course":
        data.sort(key=lambda val: val[1])
    elif on_sort == "group":
        data.sort(key=lambda val: val[2])

    return data


print(student_sorting(data))
print(student_sorting(data, "name"))
print(student_sorting(data, "course"))
print(student_sorting(data, "group"))
