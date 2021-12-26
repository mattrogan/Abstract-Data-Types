#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created By  :     Matt Rogan
# Created Date:     26/12/2021
# version = '1.0'

"""
Module implements a Queue abstract data type, for use within other programs
requiring a FIFO (LILO) structure.
"""


class Queue(object):

    def __init__(self):
        """
        Instantiation of queue object
        """

        self.state = []

    def __str__(self):
        """
        Prints the current state of the queue

        Returns:
            string representation of queue state
        """
        if self.is_empty():
            return "<>"
        else:
            return '<' + str(self.state)[1:-1] + '>'

    def enqueue(self, obj):
        """
        Adds an item `obj` to the queue

        Args:
            obj: Item to be added to the queue

        Returns:
            None
        """
        self.state.append(obj)

    def dequeue(self):
        """
        Removes item from front of queue

        Raises:
            IndexError: if the queue is empty

        Returns:
            object at front of queue
        """
        if self.is_empty():
            raise IndexError("cannot dequeue from empty queue")
        else:
            return self.state.pop(0)

    def front(self):
        """
        Returns item at the front of the queue

        Raises:
            IndexError: if the queue is empty

        Returns:
            object at front of queue

        """
        if self.is_empty():
            raise IndexError("cannot see the front of an empty queue")
        else:
            return self.state[0]

    def is_empty(self):
        """
        Predicate to return whether queue is empty or not

        Returns:
            True: if the length of `Queue.state` is zero
            False: otherwise
        """
        return self.__len__() == 0

    def __len__(self):
        """
        Returns the number of items in the queue

        Returns:
            int: number of items currently in the queue
        """
        return self.state.__len__()

    def __contains__(self, item):
        """
        Predicate method that checks if `item` is part of the queue

        Args:
            item: element to check the queue for

        Returns:
            True: if `item` is an element of `Queue.state`
            False: otherwise
        """
        return self.state.__contains__(item)
