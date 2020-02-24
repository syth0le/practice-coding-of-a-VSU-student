def water_function():
    minutes = int(input())
    if minutes >= 0:
        rezult = minutes * 12
        print(rezult)
    else:
        print('Вы ввели недопустимое число, повторите еще раз.')


print('Введите количество минут проведенное в душе:')

water_function()
while True:
    flag = input('Again? [Yes/No]: ')

    if flag == 'Yes' or flag == 'yes':
        water_function()
    else:
        break
