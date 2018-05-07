#!python

from binaryheap import BinaryMinHeap


class PriorityQueue(object):
    """ PriorityQueue: a partially ordered queue with methods to enqueue items
    in priority order and to access and dequeue its highest priority item.\n
    Item pairs are stored in a binary min heap for its efficient operations. """

    def __init__(self):
        """ Initializes priority queue. """
        self.heap = BinaryMinHeap()         # Initializes new binary min heap to store items in priority queue

    def __repr__(self):
        """ Returns string representation of priority queue. """
        return "PriorityQueue({} items, front={})".format(self.size(), self.front())

    def is_empty(self):
        """ Returns True if priority queue is empty, else returns False. """
        return self.heap.is_empty()

    def length(self):
        """ Returns number of items in priority queue. """
        return self.heap.size()

    def enqueue(self, item, priority):
        """ Inserts given item into priority queue in order according to given priority. """
        # TODO: Inserts given item into heap in order according to given priority
        

    def front(self):
        """ Returns item at front of priority queue without removing
        it, or None if priority queue is empty. """
        if self.size() == 0:
            return None
        # TODO: Returns minimum item from heap
        # ...

    def dequeue(self):
        """ Removes and returns item at front of priority queue,
        or raises ValueError if priority queue is empty. """
        if self.size() == 0:
            raise ValueError("Priority queue is empty and has no front item.")
        # TODO: Removes and returns minimum item from heap
        # ...

    def push_pop(self, item, priority):
        """ Removes and returns item at front of priority queue,
        and inserts given item in order according to given priority.\n
        This method is more efficient than calling dequeue and then enqueue."""
        if self.size() == 0:
            raise ValueError("Priority queue is empty and has no front item.")
        # TODO: Replaces and returns minimum item from heap
        # ...
