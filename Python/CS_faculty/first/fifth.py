"""5.Данное задание состоит из 2-х частей:
Реализовать любую из своих предыдущих задач с использованием итераторов (реализовать свой собственный итератор/генератор).
Реализовать любую из своих предыдущих задач с использованием декораторов (реализовать свой собственный декоратор).

Если к вашим задачам прикрутить итератор/генератор или декоратор не получается,
тогда самостоятельно придумать себе задачу (для декораторов можно «искусственную»),
где применение вышеназванных возможностей языка Python было бы оправдано.
Задачи в рамках одной группы не должны повторяться.
Сформулировать ваши задачи.

1 часть - решение через генератор задачи 4
2 часть - решение задачи 2 через декоратор
"""

text = "Пойду  гулять , теперь иду :туда,а ты   туда."


def generator_list(text):
    rules_v2 = [".", "!", "?", ",", ";"]

    for elem in rules_v2:
        text = text.replace(f" {elem}", elem).replace(elem, f"{elem} ")
        yield text


def answer_5_1(text) ->list:

    for elem in generator_list(text):
        text = elem

    text = text.replace("  ", " ").replace("  ", " ")

    return text


def answer_5_2(func) ->list:
    def wrap():
        data = func()

        transposed = list(zip(*data))
        temp = list()
        for elem in transposed:
            if elem not in temp:
                temp.append(elem)
        return list(zip(*temp))
    return wrap


@answer_5_2
def smt_func():
    matrix = [
        [0, 3, 4, 5, 4, 5, 4],
        [4, 3, 4, 5, 4, 5, 35],
        [5, 3, 4, 5, 4, 5, 34],
        [1, 3, 4, 5, 4, 5, 4]
    ]
    return matrix


print(answer_5_1(text))

print(smt_func())
