class InsertionSort(object):
    """插入排序的实现，时间复杂度为 O(n^2)

    插入排序是原址排序
    """

    def __init__(self, list_):
        self._list = list_

    def sort(self):
        a = self._list
        i = 1
        length = len(a)

        # 从第二个元素开始循环
        while i < length:
            # 记录当前元素为 key
            key = a[i]
            j = i - 1
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]
                j -= 1

            # a[j] ≤ key ，那么 key 的正确位置就是 j + 1
            a[j + 1] = key
            i += 1
