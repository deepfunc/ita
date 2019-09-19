class Stack(object):
    """栈的实现"""

    def __init__(self, n):
        self._n = n
        self._top = -1
        self._list = [None] * self._n

    def is_empty(self):
        return self._top == -1

    def pop(self):
        if self.is_empty():
            raise Exception('underflow')

        self._top -= 1
        return self._list[self._top + 1]

    def push(self, x):
        if self._top == self._n - 1:
            raise Exception('overflow')

        self._top += 1
        self._list[self._top] = x
