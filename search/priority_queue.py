import abc
from sort.heap import MaxHeap, MinHeap


class PriorityQueueBase(metaclass=abc.ABCMeta):
    def get_parent(self, i):
        return self._heap.get_parent(i)

    @property
    def heap_size(self):
        return self._heap.heap_size

    @heap_size.setter
    def heap_size(self, value):
        self._heap.heap_size = value

    def __init__(self, heap):
        self._heap = heap
        self._heap.build_heap()

    def __getitem__(self, key):
        return self._heap.list[key]

    def __setitem__(self, key, value):
        self._heap.list[key] = value

    def heapify(self, i):
        self._heap.heapify(i)

    def queue_glance(self):
        """查看当前堆的数据"""
        return self._heap.list[:self.heap_size]


class MaxPriorityQueue(PriorityQueueBase):
    """最大优先队列
    """

    def __init__(self, list_):
        super().__init__(MaxHeap(list_))

    def get_maximum(self):
        if self.heap_size < 1:
            raise Exception('queue is empty')

        return self[0]

    def extract_maximum(self):
        if self.heap_size < 1:
            raise Exception('queue is empty')

        maximum = self[0]
        self[0] = self[self.heap_size - 1]
        self.heap_size -= 1
        self.heapify(0)

        return maximum

    def increase_key(self, i, key):
        if key < self[i]:
            raise Exception('new key is smaller then current key')

        self[i] = key
        while i > 0 and self[self.get_parent(i)] < self[i]:
            self[i], self[self.get_parent(i)] = self[self.get_parent(i)], self[i]
            i = self.get_parent(i)

    def insert(self, key):
        self.heap_size += 1
        new_key = float('-inf')
        if self.heap_size > len(self._heap.list):
            self._heap.list.append(new_key)
        else:
            self[self.heap_size - 1] = new_key
        self.increase_key(self.heap_size - 1, key)


class MinPriorityQueue(PriorityQueueBase):
    """最小优先队列
    """

    def __init__(self, list_):
        super().__init__(MinHeap(list_))

    def get_minimum(self):
        if self.heap_size < 1:
            raise Exception('queue is empty')

        return self[0]

    def extract_minimum(self):
        if self.heap_size < 1:
            raise Exception('queue is empty')

        minimum = self[0]
        self[0] = self[self.heap_size - 1]
        self.heap_size -= 1
        self.heapify(0)

        return minimum

    def decrease_key(self, i, key):
        if key > self[i]:
            raise Exception('new key is bigger then current key')

        self[i] = key
        while i > 0 and self[self.get_parent(i)] > self[i]:
            self[i], self[self.get_parent(i)] = self[self.get_parent(i)], self[i]
            i = self.get_parent(i)

    def insert(self, key):
        self.heap_size += 1
        new_key = float('inf')
        if self.heap_size > len(self._heap.list):
            self._heap.list.append(new_key)
        else:
            self[self.heap_size - 1] = new_key
        self.decrease_key(self.heap_size - 1, key)
