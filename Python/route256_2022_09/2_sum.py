# Разберёмся на примере классической задачи 2-SUM. Её условие таково: дан массив целых чисел arr и целое число X, нужно
# определить, существуют ли в массиве два элемента, сумма которых в точности равна X.
import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        for i in range(10000000):
            result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return wrapper


@time_decorator
def sum_2(nums: list, target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j == i:
                continue
            if nums[i] + nums[j] == target:
                return [i, j], [nums[i], nums[j]]


@time_decorator
def twoSum(nums: list, target: int) -> list[int]:
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i

# решить через метод 2 указателей


test_array = [10, 1, 3, 5, 3, 6, 7, 23, 5, 1, 3, 8, 2, 9]

print(sum_2(test_array, 9))
print(twoSum(test_array, 9))
