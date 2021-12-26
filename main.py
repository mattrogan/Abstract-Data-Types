#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created By  :     Matt Rogan
# Created Date:     26/12/2021
# version = '1.0'

"""
Main program with procedures, allowing the user to see how abstract
data types are used and behave within a program.
"""

from stack import Stack
from queue import Queue
from graph import Graph

ITEMS_TO_USE = [1, 2, 3]


def use_stack():
    """Procedure demonstrating how a stack works"""
    print("Initialising stack...")
    s = Stack()
    print(f"Pushing items {ITEMS_TO_USE} onto stack")
    for item in ITEMS_TO_USE:
        s.push(item)
    print(s)
    print("Popping twice...")
    for _ in range(2):
        print(s.pop())
    print(s)


def use_queue():
    """Procedure demonstrating how a queue works"""
    print("Initialising queue...")
    q = Queue()
    print(f"Adding items {ITEMS_TO_USE} to queue")
    for item in ITEMS_TO_USE:
        q.enqueue(item)
    print(q)
    print("Removing twice from queue...")
    for _ in range(2):
        print(q.dequeue())
    print(q)


def use_graph():
    """Procedure demonstrating how a graph works"""
    g = Graph()
    print(f"Creating graph over {ITEMS_TO_USE} on relation <")

    for i in range(len(ITEMS_TO_USE)):
        for j in range(len(ITEMS_TO_USE)):
            if ITEMS_TO_USE[i] < ITEMS_TO_USE[j]:
                g[ITEMS_TO_USE[i]] = ITEMS_TO_USE[j]

    print(g)


# MAIN PROGRAM
if __name__ == '__main__':
    # UNCOMMENT PROCEDURE TO RUN IT:
    # use_stack()
    # use_queue()
    # use_hash_table()
    # use_graph()
    # use_tree()
    input()
