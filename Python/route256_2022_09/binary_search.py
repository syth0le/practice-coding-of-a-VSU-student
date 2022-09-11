arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 23]


def binary_search(arr: list[int], X: int) -> bool:
    if arr == [] or arr[0] > X:
        return False
    left = 0
    right = len(arr)
    while left + 1 < right:
        mid = (left + right) // 2
        if arr[mid] == X:
            return True
        elif arr[mid] <= X:
            left = mid
        else:
            right = mid
    return False


print(binary_search(arr, 4))
