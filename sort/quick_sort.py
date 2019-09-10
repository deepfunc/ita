import random


class QuickSort(object):
    """快速排序的实现
    """

    @property
    def list(self):
        return self._list

    def __init__(self, list_):
        self._list = list_[:]

    def sort1(self):
        self.sort_by_partition1(0, len(self._list) - 1)
        return self._list

    def sort2(self):
        self.sort_by_partition2(0, len(self._list) - 1)
        return self._list

    def sort1_randomized(self):
        self.sort_by_randomized_partition1(0, len(self._list) - 1)
        return self._list

    def sort_by_partition1(self, p, r):
        if p < r:
            q = self.partition1(self._list, p, r)
            self.sort_by_partition1(p, q - 1)
            self.sort_by_partition1(q + 1, r)

    def sort_by_partition2(self, p, r):
        if p < r:
            q = self.partition2(self._list, p, r)
            self.sort_by_partition2(p, q - 1)
            self.sort_by_partition2(q + 1, r)

    def sort_by_randomized_partition1(self, p, r):
        if p < r:
            q = self.randomized_partition1(self._list, p, r)
            self.sort_by_randomized_partition1(p, q - 1)
            self.sort_by_randomized_partition1(q + 1, r)

    @staticmethod
    def partition1(a, p, r):
        # 选择 r 为主元（pivot element，中心点元素）
        x = a[r]
        i = p - 1
        j = p

        # A[i] ≤ x, A[i + 1 ~ j] > x
        while j <= r - 1:
            if a[j] <= x:
                i += 1

                # 交换 i、j 的值
                a[i], a[j] = a[j], a[i]
            j += 1

        # 交换 i + 1、r 的值
        a[i + 1], a[r] = a[r], a[i + 1]
        return i + 1

    @staticmethod
    def partition2(a, p, r):
        # 选择 p 为主元
        x = a[p]
        i = p
        j = p + 1

        # A[i] ≤ x, A[i + 1 ~ j] > x
        while j <= r:
            if a[j] <= x:
                i += 1
                a[i], a[j] = a[j], a[i]
            j += 1

        # 交换 i、p 的值，注意这里是跟第一种划分不同的地方
        a[i], a[p] = a[p], a[i]
        return i

    @staticmethod
    def randomized_partition1(a, p, r):
        # exchange A[r] with A[randomized]
        i = random.randint(p, r)
        a[r], a[i] = a[i], a[r]
        return QuickSort.partition1(a, p, r)
