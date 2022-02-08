#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created By  :     Matt Rogan
# Created Date:     26/12/2021
# version = '1.0'

"""
Module implements two types of traversal recursively:
* Breadth First Traversal
* Depth First Traversal
"""

from graph import Graph
from queue import Queue
from stack import Stack

def bfs(graph, startVertex):
    """Performs a breadth first search from a given start vertex

    Args:
        graph: Graph to be searched
        startVertex: The vertex to start from

    Returns:
        visited: the list of nodes met in the traversal

    """
    queue = Queue()
    visited = []
    queue.enqueue(startVertex)

    while len(queue) > 0:

        currentNode = queue.dequeue()

        if currentNode not in visited:
            visited.append(currentNode)

        for neighbour in graph[currentNode]:
            if neighbour not in queue:
                queue.enqueue(neighbour)

    return visited


def dfs(graph, startVertex):
    """Performs a depth first search on a graph

    Args:
        graph:  Graph for the search to be performed on
        startVertex: Node to start at

    Returns:
        visited: the list of nodes visited in the search to find the target
    """
    stack = Stack()
    visited = []
    stack.push(startVertex)

    while len(stack) > 0:

        currentNode = stack.pop()

        if currentNode not in visited:
            visited.append(currentNode)

        for neighbour in graph[currentNode]:
            if neighbour not in stack:
                stack.push(neighbour)

    return visited


if __name__ == '__main__':
    exampleGraph = Graph()

    """
    Create the following graph:
    
           A 
         /   \
        B     C
       / \     \
      D   E     F 
    
    """
    # Add edges into graph
    exampleGraph['A'] = 'B'
    exampleGraph['A'] = 'C'
    exampleGraph['B'] = 'D'
    exampleGraph['B'] = 'E'
    exampleGraph['C'] = 'F'
    print(exampleGraph)

    print("BFS...")
    print(bfs(exampleGraph, 'A'))
    print("DFS...")
    print(dfs(exampleGraph, 'A'))
    input()