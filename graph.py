#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created By  :     Matt Rogan
# Created Date:     26/12/2021
# version = '1.0'

"""
Module implements a Graph, along with graph traversal algorithms
"""


class Graph(object):

    def __init__(self):
        """
        Instantiation method for `Graph` object
        """
        self.nodes = {}

    def __setitem__(self, key, value):
        """
        Creates a mapping key --> value from source (key) to target (value)

        Args:
            key:   source node in graph
            value: target node, for key to map to, in graph

        """
        # Add key -> value mapping to graph
        if key in self.nodes.keys():
            self.nodes[key].add(value)
        else:
            self.nodes[key] = {value}

        # Ensure value exists as a node
        if value not in self.nodes.keys():
            self.nodes[value] = set()

    def __getitem__(self, key):
        """
        Return values mapped to from source node `key`

        Returns:
            set: collection of values v s.t. key --> v exists in graph

        Raises:
            KeyError: if node `key` does not exist in graph
        """
        if key in self.nodes.keys():
            return self.nodes[key]
        else:
            raise KeyError("node not found in graph")

    def __str__(self):
        return self.nodes.__str__()

    def __repr__(self):
        return self.__str__()
