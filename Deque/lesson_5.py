class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        """
        Takes an item as a parameter and inserts it into the 0th index of the list
        that is representing the Deque.

        The runtime is O(n) or linear, because every time we insert into the  front of a list,
        all the other items in the list need to shift one position to the right.
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """
        Takes in an item as a parameter and appends that item to the end of the list that is representing
        the Deque.

        The runtime is constant time, or O(1).
        """
        self.items.append(item)

    def remove_front(self):
        """
        Removes ad returns the item in the 0th index of the list.

        The runtime is linear  or O(1)
        """
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        """
        Removes ad returns the last item of the list.

        The runtime is constant  or O(n)
         """
        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        """The runtime is constant  or O(n)"""
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        """The runtime is constant  or O(n)"""
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """The runtime is constant  or O(n)"""
        return len(self.items)

    def is_empty(self):
        """The runtime is constant  or O(n)"""
        return self.items == []
