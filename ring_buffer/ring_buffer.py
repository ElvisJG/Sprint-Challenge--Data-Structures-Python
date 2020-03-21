from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if storage is 0, add the item to the tail and set current to that item
        if self.storage.length == 0:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        #  if storage is less than capacity, add the item to the tail and set current to the new head
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # If storage is higher than capacity, remove from the head (oldest value), add to tail
        elif self.storage.length >= self.capacity:
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            # Just in case this is the first value and the capacity is very small make the added value the tail
            if self.storage.head == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        if self.current is None:
            return None
        iterable = self.storage.head
        list_buffer_contents.append(iterable.value)
        while iterable is not self.storage.tail:
            iterable = iterable.next

        # TODO: Your code here

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
