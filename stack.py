#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created By  :     Matt Rogan
# Created Date:     26/12/2021
# version = '1.0'

"""
Module implements a Stack abstract data type, for use within other programs
requiring a LIFO (FILO) structure.
"""


class Stack(object):

    def __init__(self):
        """
        Instantiation of stack object
        """

        self.state = []

    def __str__(self):
        """
        Prints the current state of the stack

        Returns:
            string representation of stack state
        """
        if self.is_empty():
            return "<>"
        else:
            return '<' + str(self.state)[1:-1] + '>'

    def push(self, obj):
        """
        Pushes an item `obj` onto the stack

        Args:
            obj: Item to be pushed onto the stack

        Returns:
            None
        """
        self.state.append(obj)

    def pop(self):
        """
        Pops item off the top of the stack

        Raises:
            IndexError: if the stack is empty

        Returns:
            object at top of the stack
        """
        if self.is_empty():
            raise IndexError("cannot pop from empty stack")
        else:
            return self.state.pop()

    def peek(self):
        """
        Returns the top of the stack (without removing it)

        Raises:
            IndexError: if the stack is empty

        Returns:
            object at the top of the stack
        """
        if self.is_empty():
            raise IndexError("cannot peek at top of empty stack")
        else:
            return self.state[-1]

    def is_empty(self):
        """
        Predicate to return whether stack is empty or not

        Returns:
            True: if the length of `Stack.state` is zero
            False: otherwise
        """
        return self.__len__() == 0

    def __len__(self):
        """
        Returns the number of items in the stack

        Returns:
            int: number of items currently in the stack
        """
        return self.state.__len__()

    def __contains__(self, item):
        """
        Predicate method that checks if `item` is part of the stack

        Args:
            item: element to check the stack for

        Returns:
            True: if `item` is an element of `Stack.state`
            False: otherwise
        """
        return self.state.__contains__(item)
