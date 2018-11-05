import math
from utils.random_helper import get_random_numbers_lte_100


def play():
    numbers = get_random_numbers_lte_100(10)
    print(numbers)
    _sort(numbers, 0, len(numbers) - 1)
    print(numbers)


def _sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        _sort(arr, p, q)
        _sort(arr, q + 1, r)
        _merge(arr, p, q, r)


def _merge(arr, p, q, r):
    # 两个临时数组，l_arr 包含 [p, q]，r_arr 包含 [q, r]
    # 并且每个数组要多放一个哨兵 ∞ 在最后
    n1 = q - p + 1
    n2 = r - q
    l_arr = [0] * (n1 + 1)
    r_arr = [0] * (n2 + 1)

    for i in range(n1):
        l_arr[i] = arr[p + i]
    for j in range(n2):
        r_arr[j] = arr[q + j + 1]

    # 放入哨兵
    l_arr[n1] = r_arr[n2] = math.inf

    i = 0
    j = 0
    for k in range(p, r + 1):
        if l_arr[i] <= r_arr[j]:
            arr[k] = l_arr[i]
            i += 1
        else:
            arr[k] = r_arr[j]
            j += 1
