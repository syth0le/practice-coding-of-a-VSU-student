array = [7, 4, -3, -2, 5, 0, -7 , 2]
array_2 = [5, -7, 3, 0, 1, 3, -7, 0, -2]


def generator_func(side: str, array, length: int):
    i = 0
    if side == "down":
        while i < length:
            if array[i] < 0:
                array.append(array[i])
            i += 1
    elif side == "up":
        while i < length:
            if array[i] >= 0:
                array.append(array[i])
            i += 1
    else:
        pass


def answer_1(array) -> list:
    length = len(array)
    generator_func(side="down", array=array, length=length)
    generator_func(side="up", array=array, length=length)
    return array[length:]


def decorator_func(func):
    def wrap():
        functionality = func()
        return list(zip(*functionality))
    return wrap


@decorator_func
def func():
    return [
        [0, 3, 4],
        [4, 3, 4],
        [5, 3, 4]
    ]


print(func())
print(answer_1(array))
print(answer_1(array_2))
