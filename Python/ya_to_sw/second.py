phone_number = input()


def phone_number_validation(phone_number):
    result_array = list()
    clean_number = phone_number.replace('+', '').replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
    possible_elements = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    temp = clean_number
    for elem in possible_elements:
        temp = temp.replace(elem, '')

    if temp != "":
        # print('other symbol contains')
        return "error"

    if len(clean_number) != 11:
        # print(clean_number)
        return "error"

    if not phone_number[-1].isdigit():
        return "error"

    phone_number = phone_number.replace(" ", "")

    if phone_number[0] == "8":
        result_array.append(8)
        plus = phone_number[1:].find("+")
        if plus != -1:
            return "error"
    elif phone_number[0] == "+":
        plus = phone_number[1:].find("+")
        if plus != -1:
            return "error"

        if phone_number[1] == "7":
            result_array.append(8)
        else:
            return "error"
    else:
        return "error"

    # print(phone_number)

    error_list = ['--', '-(', '(-', '-)', ')-', '))', '((', '()', ')(']
    for item in error_list:
        if phone_number.find(item) != -1:
            # print(phone_number.find(item))
            # print(item)
            return "error"

    # first_code = phone_number.find(clean_number[1])
    # last_code = phone_number.rfind(clean_number[3])
    try:
        code = phone_number.index(clean_number[1:4])
    except:
        return "error"

    if code == -1:
        # print("code error")
        return "error"

    phone_number = phone_number.replace(' ', '')
    # print(phone_number)

    if not phone_number[code - 1].isdigit():
        # print(phone_number[code-1])
        if phone_number[code - 1] == "(":
            try:
                code = phone_number.index(clean_number[1:4])
                if phone_number.index(")") != code + 3:
                    return "error"
            except:
                return "error"
        else:
            return "error"

    for elem in clean_number[1:]:
        result_array.append(elem)

    # print(len(result_array))
    if len(result_array) == 11:
        return f'{result_array[0]} ({result_array[1]}{result_array[2]}{result_array[3]}) {result_array[4]}{result_array[5]}{result_array[6]}-{result_array[7]}{result_array[8]}-{result_array[9]}{result_array[10]}'
    else:
        return "error"


print(phone_number_validation(phone_number))
# 8 (-999) 555-66-77
# 8 (9-99) 555-66-77
# 8 (99-9) 555-66-77
# 8 (999-) 555-66-77
# 8 (999)- 555-66-77
# 8 -(999) 555-66-77
# (8 (565) 678-55-88
# 6 (565) 678-55-88
# 7 (565) 678-55-88
# 8 (989( 000-55-66
