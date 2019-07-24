from .priority_queue import MaxPriorityQueue, MinPriorityQueue


class TestMaxPriorityQueue(object):
    def test_init(self):
        """测试创建的最大优先队列是否初始化为最大堆"""
        queue = MaxPriorityQueue([1, 3, 2, 4])
        assert queue.list_glance() == [4, 3, 2, 1]

    def test_get_maximum(self):
        """测试返回最大的元素"""
        queue = MaxPriorityQueue([1, 2, 3, 4, 5, 6])
        assert queue.get_maximum() == 6

    def test_insert(self):
        queue = MaxPriorityQueue([1, 2, 3])
        assert queue.list_glance() == [3, 2, 1]
