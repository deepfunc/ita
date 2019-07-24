from .priority_queue import MaxPriorityQueue, MinPriorityQueue


class TestMaxPriorityQueue(object):
    def test_init(self):
        """测试创建的最大优先队列是否初始化为最大堆"""
        queue = MaxPriorityQueue([1, 3, 2, 4])
        assert queue.list_glance() == [4, 3, 2, 1]

    def test_insert(self):
        queue = MaxPriorityQueue()
        queue.insert(1)
        queue.insert(3)
        queue.insert(2)
        queue.insert(4)
        assert queue.list_glance() == [4, 3, 2, 1]
