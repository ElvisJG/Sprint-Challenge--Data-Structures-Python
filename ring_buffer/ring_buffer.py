from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #  if storage is less than capacity, add the item to the tail and set current to the new head
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # If storage is higher than capacity, remove from the head (oldest value), add to tail
        else:
            self.current.value = item
            self.current = self.current.next or self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        iterable = self.storage.head
        while iterable is not None:
            list_buffer_contents.append(iterable.value)
            iterable = iterable.next
        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
