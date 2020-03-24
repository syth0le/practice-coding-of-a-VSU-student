from time import sleep
import numpy as np
lower_alphabet = list('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz' + ' ' * 54)
upper_alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' + ' ' * 54)
print('''This program is Vigenere cipher. you can choose mode type:
1 - encryption mode, 2 - decryption mode.
Just type sentence which you want to encrypt/decrypt, then type key word, 
choose app mode end wait for result.
''')
#sleep(1)
print('Type sentence: ', end='')
work_sentence = str(input())
#sleep(0.25)
print("Type key word: ", end='')
key_word = str(input())
#sleep(0.25)
print("Choose mode type: ", end='')
mode = input()
##
len_work = len(work_sentence)
len_key = len(key_word)
var = int(len_work / len_key) + 1
key_word = (key_word * 4)[:len_work]
massive_empty = []
s = work_sentence.count(' ')
for_empty = work_sentence
indx = 0
for i in range(s):
    indx = int(indx) + int(for_empty.index(' '))
    massive_empty.append(indx)
    for_empty = for_empty[indx + 1:]
    indx += 1
count = 0
for i in massive_empty:
    key_word = key_word[:i] + ' ' + key_word[i:]
    count += 1
##
key_word = key_word[:len(work_sentence)]
work_list = list(work_sentence)
key_list = list(key_word)
##
work_massive = []
key_massive = []
print()
print(work_sentence)
print(key_word)
print(len(work_sentence), len(key_word))
print(massive_empty)
##


def encrypt():
    for letter in work_list:
        work_num = lower_alphabet.index(letter)
        work_massive.append(work_num)
    for letter in key_list:
        key_num = lower_alphabet.index(letter)
        key_massive.append(key_num)
    a = np.array(work_massive)
    b = np.array(key_massive)
    result_massive = a + b
    temp = []
    for letter in result_massive:
        temp.append(lower_alphabet[letter])
    res_string = ''.join(temp)
    return res_string


def decrypt():
    #lower_alphabet.reverse()
    for letter in work_list:
        work_num = lower_alphabet.index(letter)
        work_massive.append(work_num)
    for letter in key_list:
        key_num = lower_alphabet.index(letter)
        key_massive.append(key_num)
    a = np.array(work_massive)
    b = np.array(key_massive)
    result_massive = a - b
    temp = []
    for letter in result_massive:
        temp.append(lower_alphabet[letter])
    res_string = ''.join(temp)
    return res_string


if int(mode) == 1:
    print("Encryption result: ", encrypt())
elif int(mode) == 2:
    print("Decryption result: ", decrypt())
else:
    print("\nThis mode is unsupportable.\nPlease, type 1 - encrypt or 2 - decrypt")
