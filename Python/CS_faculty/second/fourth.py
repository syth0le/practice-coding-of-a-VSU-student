"""выбрать (в виде списка) без повторений из текста все слова заданной длины.
 словом является непрерывная последовательность символов"""

import re
text = 'Hello!@23#!%!#&йоу соб4аки&!*!#$#%@*+_{ world!'


def answer_4(string) -> list:
    reg = re.compile('[^a-zA-Zа-яА-Я0-9 ]')

    return list(filter(lambda x: x != '', reg.sub(' ', string).split(" ")))


print(answer_4(text))
