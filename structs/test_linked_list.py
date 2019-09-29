from .linked_list import ListItem, DoublyLinkedList, SentinelDoublyLinkedList


class TestLinkedList(object):
    def test_doubly_linked_list(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.insert(ListItem(123))

        assert doubly_linked_list.search(234) is None
        assert doubly_linked_list.search(123) is not None
        assert doubly_linked_list.search(123).key == 123

        item = ListItem(666)
        doubly_linked_list.insert(item)
        assert doubly_linked_list.search(666).key == 666
        doubly_linked_list.delete(item)
        assert doubly_linked_list.search(666) is None

        item = doubly_linked_list.search(123)
        doubly_linked_list.delete(item)
        assert doubly_linked_list.search(123) is None

    def test_sentinel_doubly_linked_list(self):
        s_linked_list = SentinelDoublyLinkedList()
        s_linked_list.insert(ListItem(123))

        assert s_linked_list.search(234) == s_linked_list.nil
        assert s_linked_list.search(123) != s_linked_list.nil
        assert s_linked_list.search(123).key == 123

        item = ListItem(666)
        s_linked_list.insert(item)
        assert s_linked_list.search(666).key == 666
        s_linked_list.delete(item)
        assert s_linked_list.search(666) == s_linked_list.nil

        item = s_linked_list.search(123)
        s_linked_list.delete(item)
        assert s_linked_list.search(123) == s_linked_list.nil
