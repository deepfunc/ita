from .insertion_sort import InsertionSort


class TestInsertionSort(object):
    def test_sort(self):
        a = [5, 12, 24, 186, 32, 385, 4, 16]
        InsertionSort(a).sort()
        assert a == [4, 5, 12, 16, 24, 32, 186, 385]
