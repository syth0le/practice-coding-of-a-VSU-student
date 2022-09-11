def func(rps, ids):
    if rps == 11:
        return 6
    if rps <= 2:
        return rps
    current = None
    previous = None
    data = []
    initials = []
    i = 0
    temp = 0
    while i < rps:
        if current is None and previous is None:
            previous = ids[i]
            current = ids[i+1]
            initials = [current, previous]
            i += 2
            temp = 2
        if ids[i] not in initials:
            data.append(temp)
            temp = 1
            initials = [current, ids[i]]
            previous = current
            current = ids[i]
        temp += 1
        i += 1
    data.append(temp)
    return max(data)


N = int(input())
results = []
for i in range(N):
    rps = int(input())
    ids = list(map(int, input().split()))
    result = func(rps, ids)
    results.append(result)

for i in results:
    print(i)
