import time

houses = list(map(int, input().split()))
start = time.time()
counted = len(houses)
result = list()

for i in range(0, counted):
    if i == 0:
        current = houses[i]
        max_right = max(houses[i+1:])
        if max_right == current:
            result.append(5)
        else:
            result.append(houses[i])
    elif i + 1 == counted:
        current = houses[i]
        max_left = max(houses[:i])
        if max_left > current:
            # houses[i] = max_left
            result.append(max_left)
    else:
        current = houses[i]
        max_left = max(houses[:i])
        max_right = max(houses[i + 1:])
        min_to_build = min(max_left, max_right)
        if min_to_build > current:

            if current == houses[i+1]:
                result.append(5)
            else:
                # houses[i] = min_to_build
                result.append(min_to_build)
        else:
            result.append(houses[i])
        if max_left == max_right and max_right < 5:
            result.append(5)
            # houses[i] = 5


print(" ".join(map(str, result)))
print(time.time() - start)
# 4 2 5
# 5 2 3 1
# 4 1 2 3 5 4 5 3 2 2
# 1 3 2 3 1
# 1 1 1 1 1 2 2 2 2 3 3 3 3
# 3 3 3 3 2 2 2 2 1 1 1 1 1
