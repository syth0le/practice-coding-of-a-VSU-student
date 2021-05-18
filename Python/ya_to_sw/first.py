a, b = map(int, input().split())
adj = [[] for _ in range(a)]
help_nums = [0]*a
bool_array = [False]*a
temp = [False]
for _ in range(b):
    i, j = map(int, input().split())
    if i == j:
        temp[0] = True
    adj[j].append(i)
    help_nums[i] += 1

result = []
for _ in range(a):
    for i in range(a):
        if not bool_array[i] and help_nums[i] == 0:
            result.append(i)
            bool_array[i] = True
            for j in adj[i]:
                help_nums[j] -= 1

if len(result) == a:
    print("YES")
else:
    print("NO")
