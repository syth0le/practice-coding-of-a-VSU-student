lower_alphabet = list('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz' + ' ' * 52)
upper_alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' + ' ' * 52)


work_sentence = str(input())
key_word = str(input())


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
