class CountingSort(object):
    """计数排序的实现

    只能排序 0 ~ k区间内的整数
    时间复杂度为 O(n)，下界优先于比较排序
    """

    def __init__(self, list_):
        self._a = list_[:]
        self._k = max(self._a)

    def sort(self):
        b = [0] * len(self._a)
        c = [0] * (self._k + 1)

        # 初始化计数
        for i in range(0, len(self._a)):
            c[self._a[i]] += + 1

        # 统计 ≤ i 的个数
        for i in range(1, self._k + 1):
            c[i] += c[i - 1]

        # 把结果放置到 b
        # 放置一个计数减 1
        # 从后开始遍历是为了保证相同大小元素在结果中的相对次序
        idx = len(self._a) - 1
        while idx >= 0:
            b[c[self._a[idx]] - 1] = self._a[idx]
            c[self._a[idx]] -= 1
            idx -= 1

        return b
