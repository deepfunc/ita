class ListItem(object):
    def __init__(self, k):
        self.key = k
        self.next = None
        self.prev = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def search(self, k):
        item = self.head
        while item is not None and item.key != k:
            item = item.next
        return item

    def insert(self, item):
        item.next = self.head
        if self.head is not None:
            self.head.prev = item
        self.head = item
        item.prev = None

    def delete(self, item):
        if item.prev is not None:
            item.prev.next = item.next
        else:
            self.head = item.next
        if item.next is not None:
            item.next.prev = item.prev


class SentinelDoublyLinkedList(object):
    def __init__(self):
        nil = ListItem(None)
        nil.next = nil
        nil.prev = nil
        self.nil = nil

    def search(self, k):
        item = self.nil.next
        while item != self.nil and item.key != k:
            item = item.next
        return item

    def insert(self, item):
        item.next = self.nil.next
        self.nil.next.prev = item
        self.nil.next = item
        item.prev = self.nil

    def delete(self, item):
        item.prev.next = item.next
        item.next.prev = item.prev
