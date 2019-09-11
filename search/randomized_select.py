from sort.quick_sort import QuickSort


class RandomizedSelect(object):
    """返回序列的第 i 小元素
    """

    def __init__(self, list_):
        if not isinstance(list_, list):
            raise Exception('list_ must be a list!')
        self._list = list_

    def select(self, i):
        a = self._list
        if i <= 0:
            raise Exception('i must be greater than 0!')
        if i > len(a):
            raise Exception('i must be equal or less than %d!' % len(a))

        return self.randomized_select(a, 0, len(a) - 1, i)

    @staticmethod
    def randomized_select(a, p, r, i):
        if p == r:
            return a[p]

        q = QuickSort.randomized_partition1(a, p, r)
        k = q - p + 1
        if i == k:
            return a[q]
        elif i < k:
            return RandomizedSelect.randomized_select(a, p, q - 1, i)
        else:
            return RandomizedSelect.randomized_select(a, q + 1, r, i - k)
