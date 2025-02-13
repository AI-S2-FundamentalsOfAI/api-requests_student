# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2024 Hogeschool Utrecht
David Isaacs Paternostro en Tijmen Muller (tijmen.muller@hu.nl)
"""


def get_parent(pq, index):
    """ Return the index of the parent or None if at the root. """
    pass


def get_left_child(pq, index):
    """ Return the index of the left child if it exists, else None. """
    pass


def get_right_child(pq, index):
    """ Return the index of the right child if it exists, else None. """
    pass


def compare_at(pq, i, j):
    """ Return whether the value at index `i` is smaller than at `j`. """
    pass


def get_smallest_child(pq, index):
    """ Return the index of the smallest child. """
    pass


def top(pq):
    """ Return the index of the top of the priority queue. """
    pass


def swap(pq, i, j):
    """ Swap the two elements at index `i` and `j` in priority queue `pq`. """
    pass


def push(pq, value):
    """ Add the value to the priority queue. Make sure correct shape
    and invariant are preserved. Return True on success."""
    pass


def pop(pq, *_):
    """ Remove the top element and then reorder the priority queue so that the shape and invariant are preserved again.
    Finally, return the removed top element. """
    pass


def from_list(lst):
    pass


def from_list(lst):
    """ Convert a list into a priority queue. """
    pass
