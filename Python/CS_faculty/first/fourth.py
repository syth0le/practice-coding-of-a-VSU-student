"""4.Обработать текст следующим образом:
несколько пробелов заменить на один;
убрать все пробелы перед знаками препинания (точка, !, ?, запятая, точка с запятой),
а после данных знаков препинания должен быть пробел."""

text = "Пойду  гулять , теперь иду ;туда,а ты   туда."


def answer_4(text):
    rules_v2 = [".", "!", "?", ",", ";"]   # задаем правила замены

    for elem in rules_v2:
        text = text.replace(f" {elem}", elem).replace(elem, f"{elem} ")   # заменяем по правилам из задания

    text = text.replace("  ", " ").replace("  ", " ")  # убераем лишние пробелы

    return text   # выводим конечную строку


print(answer_4(text))
