from .radix_sort import RadixSort


class TestRadixSort(object):
    def test_sort(self):
        rs = RadixSort([123, 12, 37, 154, 86, 159])
        assert rs.sort(3) == [12, 37, 86, 123, 154, 159]
