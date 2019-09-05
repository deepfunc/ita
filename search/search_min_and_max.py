class SearchMinAndMax(object):
    """同时找到序列中的最小值和最大值
    """

    def __init__(self, list_):
        self._list = list_
        if len(self._list) <= 0:
            raise Exception('length of list must greater than zero!')

    def search(self):
        min_ = None
        max_ = None
        a = self._list
        len_ = len(a)
        idx = 0

        # set initial value for min_ and max_
        if len_ % 2 == 0:
            # len_ is even
            if a[0] <= a[1]:
                min_ = a[0]
                max_ = a[1]
            else:
                min_ = a[1]
                max_ = a[0]
            idx = 2
        else:
            min_ = a[0]
            max_ = a[0]
            idx = 1

        while idx < len_:
            if a[idx] <= a[idx + 1]:
                if a[idx] < min_:
                    min_ = a[idx]
                if a[idx + 1] > max_:
                    max_ = a[idx + 1]
            else:
                if a[idx] > max_:
                    max_ = a[idx]
                if a[idx + 1] < min_:
                    min_ = a[idx + 1]
            idx += 2

        return min_, max_
