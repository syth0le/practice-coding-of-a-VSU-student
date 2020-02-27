def sharps():
    height = int(input())
    i = 1
    if 0 <= height <= 23:
        while i <= height:
            print(" " * (height - i) + "#" * i)
            i += 1
    else:
        print("Incorrect number. Enter the number between 0 and 24")


print(
    'Enter the number between 0 and 24' '\n'
    'The program will make a triangular pyramid of gratings' '\n'
)

sharps()
while True:
    flag = input('Again? [Yes/No]: ')

    if flag == 'Yes':
        sharps()
    else:
        break
