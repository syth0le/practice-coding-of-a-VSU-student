houses = list(map(int, input().split()))


def architect(houses):
    counted = len(houses)
    result = list()

    if counted == 1:
        return 5

    for i in range(0, counted):
        if i == 0:
            current = houses[i]
            max_right = max(houses[i + 1:])
            if current >= max_right:
                result.append(5)
            else:
                result.append(current)
        elif i + 1 == counted:
            current = houses[i]
            max_left = max(houses[:i])
            if current >= max_left:
                result.append(5)
            else:
                result.append(current)
        else:
            current = houses[i]
            max_left = max(houses[:i])
            max_right = max(houses[i + 1:])
            min_to_build = min(max_left, max_right)

            if max_right == max_left:
                result.append(5)
            elif max_right == max_left == current:
                result.append(5)
            elif current == max_right and current > max_left:
                result.append(5)
            elif current == max_left and current > max_right:
                result.append(5)
            elif max_right < current < max_left or max_right > current > max_left:
                result.append(current)
            else:
                result.append(min_to_build)

    final = " ".join(map(str, result))
    return final


print(architect(houses))
# 4 2 5 -> 4 4 5
# 5 2 3 1 -> 5 3 3 1
# 4 1 2 3 5 4 5 3 2 2 -> 4 4 4 4 5 5 5 3 2 2
# 1 3 2 3 1 -> 1 5 5 5 1
# 1 1 1 1 1 2 2 2 2 3 3 3 3 -> 1 1 1 1 1 2 2 2 2 5 5 5 5
# 3 3 3 3 2 2 2 2 1 1 1 1 1 -> 5 5 5 5 2 2 2 2 1 1 1 1 1
# 1 1 1 4 4 4 1 2 1 -> 1 1 1 5 5 5 2 2 1
