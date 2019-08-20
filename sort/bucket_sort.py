import math
from .insertion_sort import InsertionSort


class BucketSort(object):
    """桶排序的实现

    该排序适合输入是均匀分布在区间 [0, 1) 的小数
    """

    def __init__(self, list_):
        self._list = list_

    def sort(self):
        a = self._list
        n = len(a)
        b = [None] * n

        for i in range(n):
            idx = math.floor(n * a[i])
            if b[idx] is None:
                b[idx] = []
            b[idx].append(a[i])

        ret = []
        for i in range(n):
            tmp_list = b[i]
            if tmp_list is not None:
                InsertionSort(tmp_list).sort()
                ret.extend(tmp_list)

        return ret
