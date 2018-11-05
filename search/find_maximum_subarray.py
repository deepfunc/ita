import math
from utils import random_helper


def play():
    numbers = random_helper.get_random_numbers_gte_negative100_lte_100(10)
    print(numbers)
    low, high, total = _find_maximum_subarray(numbers, 0, len(numbers) - 1)
    print('low: %d, high: %d, sum: %d' % (low, high, total))


def _find_maximum_subarray(arr, low, high):
    if high == low:
        return low, high, arr[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = \
            _find_maximum_subarray(arr, low, mid)
        right_low, right_high, right_sum = \
            _find_maximum_subarray(arr, mid + 1, high)
        cross_low, cross_high, cross_sum = \
            _find_maximum_crossing_subarray(arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def _find_maximum_crossing_subarray(arr, low, mid, high):
    # 最大合计一定是跨越中点的
    # 先找左半部分最大合计
    left_sum = -99999
    total = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    # 再找左半部分最大合计
    right_sum = -99999
    total = 0
    max_right = mid
    for j in range(mid + 1, high + 1):
        total += arr[j]
        if total > right_sum:
            right_sum = total
            max_right = j

    return max_left, max_right, left_sum + right_sum
