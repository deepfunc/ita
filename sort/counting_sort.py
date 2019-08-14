class CountingSort(object):
    """计数排序的实现

    只能排序 0 ~ k区间内的整数
    时间复杂度为 O(n)，下界优先于比较排序
    """

    def __init__(self, list_):
        self._a = list_[:]

    def sort(self):
        a = self._a
        k = max(a)
        b = [0] * len(a)
        c = [0] * (k + 1)

        # 初始化计数
        for i in range(0, len(a)):
            c[a[i]] += + 1

        # 统计 ≤ i 的个数
        for i in range(1, k + 1):
            c[i] += c[i - 1]

        # 把结果放置到 b
        # 放置一个后计数减 1
        # 从后开始遍历是为了保证相同大小元素在结果中的相对顺序
        idx = len(a) - 1
        while idx >= 0:
            b[c[a[idx]] - 1] = a[idx]
            c[a[idx]] -= 1
            idx -= 1

        return b


class CountingSortByKey(object):
    """按 key 进行计数排序

    传进来的是个 dict list，每个 dict 按照 key 进行排序
    """

    def __init__(self, list_, key):
        self._a = list_[:]
        self._key = key

    def sort(self):
        a = self._a
        key = self._key
        largest = max(a, key=lambda d: d[key])
        k = largest[key]
        b = [0] * len(a)
        c = [0] * (k + 1)

        # 初始化计数
        for i in range(0, len(a)):
            c[a[i][key]] += + 1

        # 统计 ≤ i 的个数
        for i in range(1, k + 1):
            c[i] += c[i - 1]

        # 把结果放置到 b
        # 放置一个后计数减 1
        # 从后开始遍历是为了保证相同大小元素在结果中的相对顺序
        idx = len(a) - 1
        while idx >= 0:
            b[c[a[idx][key]] - 1] = a[idx]
            c[a[idx][key]] -= 1
            idx -= 1

        return b
