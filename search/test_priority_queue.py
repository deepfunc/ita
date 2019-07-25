import pytest
from .priority_queue import MaxPriorityQueue, MinPriorityQueue


class TestMaxPriorityQueue(object):
    def test_init(self):
        """测试创建的最大优先队列是否初始化为最大堆"""
        queue = MaxPriorityQueue([1, 3, 2, 4])
        assert queue.queue_glance() == [4, 3, 2, 1]

    def test_get_maximum(self):
        """测试返回最大元素"""
        queue = MaxPriorityQueue([1, 2, 3, 4, 5, 6])
        assert queue.get_maximum() == 6
        queue = MaxPriorityQueue([10, 100, 123, 789, 456, 300, 241])
        assert queue.get_maximum() == 789

    def test_extract_maximum(self):
        """测试抽取最大元素"""
        queue = MaxPriorityQueue([1, 2, 3])
        assert queue.extract_maximum() == 3
        assert queue.queue_glance() == [2, 1]
        assert queue.heap_size == 2
        queue.insert(6)
        assert queue.queue_glance() == [6, 1, 2]
        assert queue.heap_size == 3

    def test_increase_key(self):
        """测试增加元素的值"""
        queue = MaxPriorityQueue([1, 2, 3, 4])
        assert queue.queue_glance() == [4, 2, 3, 1]
        with pytest.raises(Exception) as e:
            queue.increase_key(2, 1)
        assert 'smaller' in str(e.value)
        queue.increase_key(2, 6)
        assert queue.queue_glance() == [6, 2, 4, 1]
        queue.increase_key(3, 66)
        assert queue.queue_glance() == [66, 6, 4, 2]

    def test_insert(self):
        """测试增加新的元素"""
        queue = MaxPriorityQueue([])
        assert queue.queue_glance() == []
        assert queue.heap_size == 0

        queue.insert(1)
        assert queue.queue_glance() == [1]
        assert queue.heap_size == 1

        queue.insert(7)
        assert queue.queue_glance() == [7, 1]
        assert queue.heap_size == 2

        queue.insert(6)
        assert queue.queue_glance() == [7, 1, 6]
        assert queue.heap_size == 3

        queue.insert(99)
        assert queue.queue_glance() == [99, 7, 6, 1]
        assert queue.heap_size == 4


class TestMinPriorityQueue(object):
    def test_init(self):
        """测试创建的最小优先队列是否初始化为最小堆"""
        queue = MinPriorityQueue([4, 3, 2, 1])
        assert queue.queue_glance() == [1, 3, 2, 4]
