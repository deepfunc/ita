import abc


class HeapBase(metaclass=abc.ABCMeta):
    @staticmethod
    def _get_parent(i):
        """获得父节点下标"""
        return (i - 1) // 2

    @staticmethod
    def _get_left(i):
        """获得左孩子节点的下标"""
        return 2 * i + 1

    @staticmethod
    def _get_right(i):
        """获得右孩子节点的下标"""
        return 2 * i + 2

    def __init__(self, list_):
        self._list = list_[:]
        self._heap_size = len(self._list)

    @abc.abstractmethod
    def _heapify(self, i):
        pass

    @abc.abstractmethod
    def _build_heap(self):
        pass

    @abc.abstractmethod
    def sort(self):
        pass


class MaxHeap(HeapBase):
    """最大堆的实现

    父节点数值 ≥ 孩子节点数值
    """

    def _heapify(self, i):
        """维护最大堆的性质，对可能违反的节点逐级下降"""
        largest = i
        left = self._get_left(i)
        right = self._get_right(i)
        if left <= self._heap_size - 1 and self._list[left] > self._list[largest]:
            largest = left
        if right <= self._heap_size - 1 and self._list[right] > self._list[largest]:
            largest = right
        if largest != i:
            self._list[i], self._list[largest] = self._list[largest], self._list[i]
            self._heapify(largest)

    def _build_heap(self):
        """建堆，注意数组下标是从 0 开始的"""
        self.__heap_size = len(self._list)
        parent = self._get_parent(self._heap_size - 1)
        while parent >= 0:
            self._heapify(parent)
            parent -= 1

    def sort(self):
        """最大堆排序，上面一大堆都是为这一步做准备啦"""
        self._build_heap()
        idx = len(self._list) - 1

        # 一直迭代到第二个元素
        while idx >= 1:
            # 交换第一个元素（最大）与最后一个，并维护最大堆特性
            self._list[0], self._list[idx] = self._list[idx], self._list[0]
            self._heap_size -= 1
            self._heapify(0)
            idx -= 1

        return self._list


class MinHeap(HeapBase):
    """最小堆的实现

    父节点数值 ≤ 孩子节点数值
    """

    def _heapify(self, i):
        smallest = i
        left = self._get_left(i)
        right = self._get_right(i)
        if left <= self._heap_size - 1 and self._list[left] < self._list[smallest]:
            smallest = left
        if right <= self._heap_size - 1 and self._list[right] < self._list[smallest]:
            smallest = right
        if smallest != i:
            self._list[i], self._list[smallest] = self._list[smallest], self._list[i]
            self._heapify(smallest)

    def _build_heap(self):
        self.__heap_size = len(self._list)
        parent = self._get_parent(self._heap_size - 1)
        while parent >= 0:
            self._heapify(parent)
            parent -= 1

    def sort(self):
        self._build_heap()
        idx = len(self._list) - 1

        while idx >= 1:
            # 交换第一个元素（最小）与最后一个，并维护最小堆特性
            self._list[0], self._list[idx] = self._list[idx], self._list[0]
            self._heap_size -= 1
            self._heapify(0)
            idx -= 1

        return self._list[::-1]
