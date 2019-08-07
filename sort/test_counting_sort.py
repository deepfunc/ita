from .counting_sort import CountingSort


class TestCountingSort(object):
    def test_sort(self):
        cs = CountingSort([2, 5, 3, 0, 2, 3, 0, 3])
        assert cs.sort() == [0, 0, 2, 2, 3, 3, 3, 5]
        cs = CountingSort([23, 32, 12, 47, 28, 6, 12, 27])
        assert cs.sort() == [6, 12, 12, 23, 27, 28, 32, 47]
