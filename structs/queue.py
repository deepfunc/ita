class Queue(object):
    """FIFO 队列的实现

    head 指向对头元素，tail 指向下一个新元素将要插入的位置。
    注意，最多只能存在 n - 1 个元素。
    """

    def __init__(self, n):
        self._n = n
        self._list = [None] * self._n
        self._head = self._tail = 0

    def en_queue(self, x):
        if self.is_full():
            raise Exception('overflow')

        self._list[self._tail] = x
        self._tail = (self._tail + 1 if self._tail != self._n - 1 else 1)

    def de_queue(self):
        if self.is_empty():
            raise Exception('underflow')

        x = self._list[self._head]
        self._head = (self._head + 1 if self._head != self._n - 1 else 1)

        return x

    def is_empty(self):
        return self._head == self._tail

    def is_full(self):
        next_tail = self._tail + 1 if self._tail != self._n - 1 else 1
        return next_tail == self._head
