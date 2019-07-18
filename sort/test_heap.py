from .heap import HeapBase, MaxHeap


class TestHeapBase(object):
    def test_get_parent(self):
        assert HeapBase._get_parent(1) == 0
        assert HeapBase._get_parent(2) == 0
        assert HeapBase._get_parent(3) == 1
        assert HeapBase._get_parent(5) == 2

    def test_get_left(self):
        assert HeapBase._get_left(0) == 1
        assert HeapBase._get_left(2) == 5
        assert HeapBase._get_left(3) == 7

    def test_get_right(self):
        assert HeapBase._get_right(0) == 2
        assert HeapBase._get_right(1) == 4
        assert HeapBase._get_right(2) == 6


class TestMaxHeap(object):
    def test_heapify(self):
        list_ = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        max_heap = MaxHeap(list_)
        max_heap._heapify(1)
        assert max_heap._list == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

    def test_build_heap(self):
        list_ = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        max_heap = MaxHeap(list_)
        max_heap._build_heap()
        assert max_heap._list == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
