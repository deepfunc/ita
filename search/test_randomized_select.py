import pytest
from .randomized_select import RandomizedSelect


class TestRandomizedSelect(object):
    def test_select(self):
        rs = RandomizedSelect([1, 5, 3, 12, 7, 14, 28])
        assert rs.select(1) == 1
        assert rs.select(2) == 3
        assert rs.select(3) == 5
        assert rs.select(4) == 7
        assert rs.select(5) == 12
        assert rs.select(6) == 14
        assert rs.select(7) == 28
        with pytest.raises(Exception, match=r'greater than'):
            rs.select(0)
        with pytest.raises(Exception, match=r'equal or less than'):
            rs.select(99)
