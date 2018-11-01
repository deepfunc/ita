from utils.random_helper import get_random_numbers_lte_100


def play():
    numbers = get_random_numbers_lte_100(10)
    print(numbers)
    sort(numbers)
    print(numbers)


def sort(arr):
    # 从第二个元素开始循环
    for i in range(1, len(arr)):
        # 记录当前元素为 key
        key = arr[i]
        j = i - 1

        # 从当前元素往前面判断，比 key 大的顺次往后移
        # arr[i] 已被记住为 key ，没事
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # arr[j] <= key ，那么 key 的正确位置就是 j + 1
        arr[j + 1] = key
