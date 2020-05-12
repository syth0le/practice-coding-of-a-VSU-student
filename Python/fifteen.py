import numpy as np
import time

while True:
    try:
        workNum = int(input("Choose map size (enter 3 or 4): "))
        if workNum == 3 or workNum == 4:
            print("Well, initialisation...\n")
            time.sleep(0.5)
            break
        else:
            print("Enter correct number.\n")
    except (TypeError, ValueError):
        print("WARNING.\nIncorrect input. Please, read the description and enter needful number.\n")
massive = []


def init():
    size = workNum
    k = 1
    for i in range(size):
        massive.append([0] * size)
    for i in range(size):
        for j in range(size):
            massive[i][j] = k
            k += 1
    massive[0][0], massive[0][1] = massive[0][1], massive[0][0]
    massive[-1][-1] = str('_')
    #massive[-1][-1], massive[-1][-2] = massive[-1][-2], massive[-1][-1] # for check


def draw():
    for i in massive:
        print()
        for j in i:
            print(j, end='     ')


init()
draw()


def move():
    rerun = 0
    while rerun == 0:
        try:
            inNum = int(input("\nNumber: "))
            if 0 < int(inNum) < workNum ** 2:
                print("Well, initialisation...\n")
                rerun = 1
            else:
                print("Enter correct number.\n")
        except (TypeError, ValueError):
            print("WARNING.\nIncorrect input. Please, read the description and enter needful number.\n")
    number = inNum
    i = 0
    numMassive = []
    arrMassive = []
    for var in massive:  # searching index of number
        i += 1
        j = 0
        for num in var:
            if number == num:
                column = j
                row = i - 1
                numMassive.append(column)
                numMassive.append(row)
            j += 1
    i = 0
    for var in massive:  # searching index of empty part of matrix
        i += 1
        j = 0
        for symbol in var:
            if symbol == '_':
                colSymb = j
                rowSymb = i - 1
                arrMassive.append(colSymb)
                arrMassive.append(rowSymb)
            j += 1
    # connecting numpy for count difference between arrMassive and numMassive
    a = np.array(numMassive)
    b = np.array(arrMassive)
    c = a - b

    if all(c == (1, 0)):
        massive[row][column - 1], massive[row][column] = massive[row][column], massive[row][column - 1]
    elif all(c == (0, 1)):
        massive[row - 1][column], massive[row][column] = massive[row][column], massive[row - 1][column]
    elif all(c == (0, -1)):
        massive[row + 1][column], massive[row][column] = massive[row][column], massive[row + 1][column]
    elif all(c == (-1, 0)):
        massive[row][column + 1], massive[row][column] = massive[row][column], massive[row][column + 1]


def won():
    status = 0
    current = 0
    check = []
    for arr in massive:
        for elem in arr:
            check.append(elem)
    check = check[:-1]
    for elem in check:
        if isinstance(elem, int) and elem > current:
            current = elem
            status = 0
        else:
            status = 1
            break
    return status


while True:
    if won() == 0:
        print("\nCongratulations!!! U won.")
        break
    move()
    draw()
