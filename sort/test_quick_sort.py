from .quick_sort import QuickSort


class TestQuickSort(object):
    def test_partition1(self):
        """测试第一种划分，主元是 A[r]"""
        qs = QuickSort([16, 5, 4, 3, 2, 7])
        q = qs.partition1(0, 5)
        assert q == 4
        assert qs.list == [5, 4, 3, 2, 7, 16]

    def test_sort1(self):
        """测试按第一种划分排序"""
        qs = QuickSort([16, 5, 4, 3, 2, 7, 1, 66, 17])
        assert qs.sort1() == [1, 2, 3, 4, 5, 7, 16, 17, 66]

    def test_partition2(self):
        """测试第一种划分，主元是 A[p]"""
        qs = QuickSort([16, 5, 4, 3, 2, 7])
        q = qs.partition2(0, 5)
        assert q == 5
        assert qs.list == [7, 5, 4, 3, 2, 16]

    def test_sort2(self):
        """测试按第二种划分排序"""
        qs = QuickSort([16, 5, 4, 3, 2, 7, 1, 66, 17])
        assert qs.sort2() == [1, 2, 3, 4, 5, 7, 16, 17, 66]
