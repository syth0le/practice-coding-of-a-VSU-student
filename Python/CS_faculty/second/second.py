"""создать новый двумерный массив элементов, развернув переданный массив вокруг главной диагонали"""
matrix = [
    [0, 3, 4],
    [4, 3, 4],
    [5, 3, 4]
]


def answer_2(array) -> list:
    return list(zip(*array))


print(answer_2(matrix))
