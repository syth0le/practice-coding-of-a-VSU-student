alphabet = list("abcdefghijklmnopqrstuvwxyza bc ")
print("Type the sentence please:", end=" ")
input_string = input()
work_list = list(input_string.lower())
res_massive = []
num_massive = []
for letter in work_list:
    inx = alphabet.index(letter)
    if letter == " ":
        num_massive.append(work_list.index(letter))
    res_massive.append(alphabet[inx + 3])
res_string = ''.join(res_massive)
print("Result: ", res_string)
