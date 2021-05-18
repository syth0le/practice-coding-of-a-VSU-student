array = [7, 4, -3, -2, 5, 0, -7 , 2]
array_2 = [5, -7, 3, 0, 1, 3, -7, 0, -2]


def answer_1(array) -> list:
    i = 0
    length = len(array)
    while i < length:
        if array[i] < 0:
            array.append(array[i])
        i += 1

    i = 0
    while i < length:
        if array[i] >= 0:
            array.append(array[i])
        i += 1

    return array[length:]


print(answer_1(array))
