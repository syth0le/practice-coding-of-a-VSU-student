from time import sleep
print('''This program is Caesar cipher. you can choose mode type:
1 - encryption mode, 2 - decryption mode.
Just type sentence which you want to encrypt/decrypt,
then choose mode end wait for result.
''')
sleep(0.75)
alphabet = list("abcdefghijklmnopqrstuvwxyzabc    ")
print("Type the sentence please:", end=" ")
sleep(0.4)
input_string = input()
work_list = list(input_string.lower())
res_massive = []
num_massive = []
print("Choose mode, please",
      "(1 - encryption mode, 2 - decryption mode):", end=" ")
mode = input()
sleep(0.5)


def encrypt():
    for letter in work_list:
        inx = alphabet.index(letter)
        if letter == " ":
            num_massive.append(work_list.index(letter))
        res_massive.append(alphabet[inx + 3])
    res_string = ''.join(res_massive)
    return res_string


def decrypt():
    alphabet.reverse()
    new_alphabet = alphabet[3:] + alphabet[:3]
    for letter in work_list:
        inx = new_alphabet.index(letter)
        if letter == " ":
            num_massive.append(work_list.index(letter))
        res_massive.append(new_alphabet[inx + 3])
    res_string = ''.join(res_massive)
    return res_string


if int(mode) == 1:
    print("Result: ", encrypt())
elif int(mode) == 2:
    print("Result: ", decrypt())
else:
    print("Unsupportable mode. Try again.")

sleep(1000)
