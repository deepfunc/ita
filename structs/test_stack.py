import pytest
from .stack import Stack


class TestStack(object):
    def test_push_and_pop(self):
        stack = Stack(10)
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    def test_overflow(self):
        stack = Stack(1)
        stack.push(1)

        with pytest.raises(Exception, match=r'overflow'):
            stack.push(2)

    def test_underflow(self):
        stack = Stack(10)
        stack.push(6)
        assert stack.pop() == 6

        with pytest.raises(Exception, match=r'underflow'):
            stack.pop()
