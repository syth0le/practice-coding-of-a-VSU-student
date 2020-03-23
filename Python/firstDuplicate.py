num_list = list(map(int, input().split()))
num_set = set()
result_list = []
for elem in num_list:
    if elem in num_set:
        result_list.append(elem)
    else:
        num_set.add(elem)
if len(result_list) != 0:
    print(result_list[0])
else:
    print(-1)
