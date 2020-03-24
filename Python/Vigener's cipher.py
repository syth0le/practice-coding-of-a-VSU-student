from time import sleep
lower_alphabet = list('abcdefghijklmnopqrstuvwxyz')
upper_alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print('''This program is Vigenere cipher. you can choose mode type:
1 - encryption mode, 2 - decryption mode.
Just type sentence which you want to encrypt/decrypt, then type key word, 
choose app mode end wait for result.
''')
sleep(1)
print('Type sentence: ', end='')
work_sentence = str(input())
sleep(0.25)
print("Type key word: ", end='')
key_word = str(input())
sleep(0.25)
print("Choose mode type:", end='')
mode = input()


def encrypt():
    return 1


def decrypt():
    return 2


if mode == 1:
    print(encrypt())
elif mode == 0:
    print(decrypt())
else:
    print("\nThis mode is unsupportable.\nPlease, type 1 - encrypt or 2 - decrypt")
