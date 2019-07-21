from sort.heap import MaxHeap, MinHeap


class MaxPriorityQueue(object):
    def __int__(self):
        self._maxHeap = MaxHeap([])

    def get_maximum(self):
        if self._maxHeap.heap_size < 1:
            raise Exception('queue is empty')

        return self._maxHeap.list[0]

    def extract_maximum(self):
        if self._maxHeap.heap_size < 1:
            raise Exception('queue is empty')

        maximum = self._maxHeap.list[0]
        self._maxHeap.list[0] = self._maxHeap.list[self._maxHeap.heap_size - 1]
        self._maxHeap.heap_size -= 1
        self._maxHeap.heapify(0)

        return maximum

    def increase_key(self, i, key):
        if key < self._maxHeap.list[i]:
            raise Exception('new key is smaller then current key')

        while i > 0 and self._maxHeap.list[MaxHeap.get_parent(i)] < self._maxHeap.list[i]:
            self._maxHeap.list[i], self._maxHeap.list[MaxHeap.get_parent(i)] = \
                self._maxHeap.list[MaxHeap.get_parent(i)], self._maxHeap.list[i]
            i = MaxHeap.get_parent(i)

    def insert(self, key):
        self._maxHeap.heap_size += 1
        self._maxHeap.list[self._maxHeap.heap_size - 1] = float('-inf')
        self.increase_key(self._maxHeap.heap_size - 1, key)


class MinPriorityQueue(object):
    def __int__(self):
        self._minHeap = MinHeap([])

    def get_minimum(self):
        if self._minHeap.heap_size < 1:
            raise Exception('queue is empty')

        return self._minHeap.list[0]

    def extract_minimum(self):
        if self._minHeap.heap_size < 1:
            raise Exception('queue is empty')

        minimum = self._minHeap.list[0]
        self._minHeap.list[0] = self._minHeap.list[self._minHeap.heap_size - 1]
        self._minHeap.heap_size -= 1
        self._minHeap.heapify(0)

        return minimum

    def decrease_key(self, i, key):
        if key > self._minHeap.list[i]:
            raise Exception('new key is bigger then current key')

        while i > 0 and self._minHeap.list[MinHeap.get_parent(i)] > self._minHeap.list[i]:
            self._minHeap.list[i], self._minHeap.list[MinHeap.get_parent(i)] = \
                self._minHeap.list[MinHeap.get_parent(i)], self._minHeap.list[i]
            i = MinHeap.get_parent(i)

    def insert(self, key):
        self._minHeap.heap_size += 1
        self._minHeap.list[self._minHeap.heap_size - 1] = float('inf')
        self.decrease_key(self._minHeap.heap_size - 1, key)
