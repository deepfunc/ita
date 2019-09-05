from .search_min_and_max import SearchMinAndMax


class TestSearchMinAndMax(object):
    def test_search(self):
        min_, max_ = SearchMinAndMax([2]).search()
        assert min_ == 2
        assert max_ == 2

        min_, max_ = SearchMinAndMax([3, 123]).search()
        assert min_ == 3
        assert max_ == 123

        min_, max_ = SearchMinAndMax([1, 5, -12, 327]).search()
        assert min_ == -12
        assert max_ == 327

        min_, max_ = SearchMinAndMax([6, 32, 47, 114, -1, 378, 542, 18]).search()
        assert min_ == -1
        assert max_ == 542
