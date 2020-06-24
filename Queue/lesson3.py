class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """ This method takes an item and inserts that item into the 0th index of
        the list that is representing the Queue

        The runtime is 0(n), or linear time, because inserting into the 0th index of a list
        forces all the other items in the list to move one index to the right.
        """
        self.items.insert(0, item)

    def de_queue(self):
        """   Returns and remove the front-most item of the Queue, which is represented by
        the last item in the list.

        The runtime is constant time or O(1), because indexing to the end of the list
        happens in constant time.
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """ Returns the last item in the list which represents the front-most item in the Queue.

        The runtime is constant time, or O(1), because we`re just indexing to the last item of the list
        and returning the value found there.
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the size of Queue, which is represent by the length of the list.

        The runtime is O(1), or constant time, because we`re only returning the length.
        """
        return len(self.items)

    def is_empty(self):
        """Returns a Boolean value expressing whether or not the list representing
        the Queue is empty.

        The runtime is O(1), or constant time, because we`re only checking for equality.
        """
        return self.items == []
