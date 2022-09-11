def func(rps, ids):
    if rps <= 2:
        return rps
    id1, id2 = ids[0], ids[1]
    indId2 = 1
    lenOtr = 0
    if id1 != 0:
        lenOtr += 1
    if id1 != 0:
        lenOtr += 1
    maxLen = lenOtr
    i = 2
    while i < rps:
        if ids[i] == 0:
            continue
        elif id2 == id1 and ids[i] != id1:
            lenOtr += 1
            if maxLen < lenOtr:
                maxLen = lenOtr

            id2 = ids[i]
            indId2 = i
        elif ids[i] != id1 and ids[i] != id2:
            if maxLen < lenOtr:
                maxLen = lenOtr

            lenOtr = i - indId2 + 1
            indId2 = i
            id1 = id2
            id2 = ids[i]
        elif ids[i] == id2:
            lenOtr += 1
            if maxLen < lenOtr:
                maxLen = lenOtr

        elif ids[i] == id1:
            lenOtr += 1
            if maxLen < lenOtr:
                maxLen = lenOtr

            id1, id2 = id2, id1
            indId2 = i

    return maxLen


N = int(input())
results = []
for i in range(N):
    rps = int(input())
    ids = list(map(int, input().split()))
    result = func(rps, ids)
    results.append(result)

for i in results:
    print(i)
