def decode(s):
    length = len(s)
    temp = ''
    i = 0
    while i < length:
        if s[i:i+2] == '00':
            temp += 'a'
            i += 2
        elif s[i:i+3] == '100':
            temp += 'b'
            i += 3
        elif s[i:i+3] == '101':
            temp += 'c'
            i += 3
        elif s[i:i+2] == '11':
            temp += 'd'
            i += 2
        else:
            i += 1
    return temp


N = int(input())
results = []
for i in range(N):
    temp = input()
    decoded = decode(temp)
    results.append(decoded)

for i in results:
    print(i)
