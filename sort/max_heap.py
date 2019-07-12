class MaxHeap(object):
    """最大堆的实现

    父节点数值 >= 孩子节点数值
    """

    def __init__(self, list_):
        self.__list = list_[:]
        self.__heap_size = -1

    @staticmethod
    def __get_parent(i):
        """获得父节点下标"""
        return (i - 1) // 2

    @staticmethod
    def __get_left(i):
        """获得左孩子节点的下标"""
        return 2 * i + 1

    @staticmethod
    def __get_right(i):
        """获得右孩子节点的下标"""
        return 2 * i + 2

    def __max_heapify(self, i):
        """维护最大堆的性质，对可能违反的节点逐级下降"""
        left = self.__get_left(i)
        right = self.__get_right(i)
        largest = i
        if left <= self.__heap_size and self.__list[left] > self.__list[i]:
            largest = left
        if right <= self.__heap_size and self.__list[right] > self.__list[largest]:
            largest = left
        if largest != i:
            self.__list[i], self.__list[largest] = self.__list[largest], self.__list[i]
            self.__max_heapify(largest)

    def __build_max_heap(self):
        """建堆，注意数组下标是从 0 开始的"""
        self.__heap_size = len(self.__list)
        parent = self.__get_parent(self.__heap_size)
        while parent >= 0:
            self.__max_heapify(parent)
            parent -= 1

    def heap_sort(self):
        """最大堆排序，上面一大堆都是为这一步做准备啦"""
        self.__build_max_heap()
        pass
