from .counting_sort import CountingSort, CountingSortByKey


class TestCountingSort(object):
    def test_sort(self):
        cs = CountingSort([2, 5, 3, 0, 2, 3, 0, 3])
        assert cs.sort() == [0, 0, 2, 2, 3, 3, 3, 5]
        cs = CountingSort([23, 32, 12, 47, 28, 6, 12, 27])
        assert cs.sort() == [6, 12, 12, 23, 27, 28, 32, 47]

    def test_sort_by_key(self):
        list_ = [
            {'name': 'A', 'key': 65},
            {'name': 'K', 'key': 75},
            {'name': 'G', 'key': 71},
            {'name': 'Y', 'key': 89},
            {'name': 'W', 'key': 87},
            {'name': 'C', 'key': 67}
        ]
        cs = CountingSortByKey(list_, 'key')
        ret = cs.sort()
        ret_names = [d['name'] for d in ret]
        assert ret_names == ['A', 'C', 'G', 'K', 'W', 'Y']
