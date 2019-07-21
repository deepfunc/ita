from .heap import HeapBase, MaxHeap, MinHeap


class TestHeapBase(object):
    def test_get_parent(self):
        assert HeapBase.get_parent(1) == 0
        assert HeapBase.get_parent(2) == 0
        assert HeapBase.get_parent(3) == 1
        assert HeapBase.get_parent(5) == 2

    def test_get_left(self):
        assert HeapBase.get_left(0) == 1
        assert HeapBase.get_left(2) == 5
        assert HeapBase.get_left(3) == 7

    def test_get_right(self):
        assert HeapBase.get_right(0) == 2
        assert HeapBase.get_right(1) == 4
        assert HeapBase.get_right(2) == 6


class TestMaxHeap(object):
    def test_heapify(self):
        list_ = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        max_heap = MaxHeap(list_)
        max_heap.heapify(1)
        assert max_heap.list == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

    def test_build_heap(self):
        list_ = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        max_heap = MaxHeap(list_)
        max_heap.build_heap()
        assert max_heap.list == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

    def test_sort(self):
        list_ = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        max_heap = MaxHeap(list_)
        assert max_heap.sort() == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]


class TestMinHeap(object):
    def test_heapify(self):
        list_ = [16, 4, 5, 14, 7]
        min_heap = MinHeap(list_)
        min_heap.heapify(0)
        assert min_heap.list == [4, 7, 5, 14, 16]

    def test_build_heap(self):
        list_ = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        min_heap = MinHeap(list_)
        min_heap.build_heap()
        assert min_heap._list == [1, 2, 3, 8, 4, 9, 10, 14, 16, 7]

    def test_sort(self):
        list_ = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        min_heap = MinHeap(list_)
        assert min_heap.sort() == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
