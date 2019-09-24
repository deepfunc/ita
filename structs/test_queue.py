import pytest
from .queue import Queue


class TestQueue(object):
    def test_queue(self):
        q = Queue(6)
        q.en_queue(3)
        q.en_queue(2)
        q.en_queue(1)

        assert q.de_queue() == 3
        assert q.de_queue() == 2
        assert q.de_queue() == 1

    def test_overflow(self):
        q = Queue(2)
        q.en_queue(1)

        with pytest.raises(Exception, match=r'overflow'):
            q.en_queue(1)

    def test_underflow(self):
        q = Queue(10)
        q.en_queue(1)
        q.de_queue()

        with pytest.raises(Exception, match=r'underflow'):
            q.de_queue()
