# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2024 Hogeschool Utrecht
David Isaacs Paternostro en Tijmen Muller (tijmen.muller@hu.nl)
"""

import random
import priority_queue


def check_invariant(pq):
    """ Check if invariant is preserved. """
    for i in range(1, len(pq)):
        assert pq[i] >= pq[priority_queue.get_parent(pq, i)]


def test_get_parent():
    pq = [2, 6, 3, 10, 12, 5]
    assert priority_queue.get_parent(pq, 0) is None
    assert priority_queue.get_parent(pq, 5) == 2
    assert priority_queue.get_parent(pq, 4) == 1


def test_get_childs():
    pq = [2, 6, 3, 10, 12, 5]
    assert priority_queue.get_right_child(pq, 2) is None
    assert priority_queue.get_right_child(pq, 0) == 2
    assert priority_queue.get_right_child(pq, 5) is None

    assert priority_queue.get_left_child(pq, 0) == 1
    assert priority_queue.get_left_child(pq, 2) == 5
    assert priority_queue.get_left_child(pq, 5) is None


def test_compare_at():
    pq = [2, 6, 3, 10, 12, 5]
    assert priority_queue.compare_at(pq, 0, 3)
    assert not priority_queue.compare_at(pq, 3, 0)
    assert not priority_queue.compare_at(pq, None, 0)
    assert priority_queue.compare_at(pq, 0, None)


def test_get_smallest_child():
    pq = [2, 6, 3, 10, 12, 5]
    assert priority_queue.get_smallest_child(pq, 0) == 2
    assert priority_queue.get_smallest_child(pq, 1) == 3
    assert priority_queue.get_smallest_child(pq, 2) == 5
    assert priority_queue.get_smallest_child(pq, 5) is None


def test_top():
    pq = [2, 6, 3, 10, 12, 5]
    # assert priority_queue.top(pq) == 2 # Fout?
    assert priority_queue.top(pq) == 0
    assert pq == [2, 6, 3, 10, 12, 5]


def test_swap():
    pq = [2, 6, 3, 10, 12, 5]
    priority_queue.swap(pq, 0, -1)
    assert pq == [5, 6, 3, 10, 12, 2]
    priority_queue.swap(pq, 0, 1)
    assert pq == [6, 5, 3, 10, 12, 2]
    priority_queue.swap(pq, 0, 5)
    assert pq == [2, 5, 3, 10, 12, 6]


def test_insert():
    pq = [2, 6, 3, 10, 12, 5]
    priority_queue.push(pq, 1)
    assert pq == [1, 6, 2, 10, 12, 5, 3]

    # Simulated test
    for v in random.choices(range(100), k=100):
        priority_queue.push(pq, v)
        check_invariant(pq)


def test_pop():
    pq = [2, 6, 3, 10, 12, 5]
    v = priority_queue.pop(pq)
    assert v == 2
    check_invariant(pq)
    assert pq == [3, 6, 5, 10, 12]

    pq = [2, 3, 10]
    v = priority_queue.pop(pq)
    assert v == 2
    check_invariant(pq)
    assert pq == [3, 10]

    # Simulated test
    # Create queue
    for v in random.choices(range(100), k=100):
        priority_queue.push(pq, v)

    # Pop queue
    for _ in range(len(pq)):
        min_val = min(pq)
        val = priority_queue.pop(pq)
        assert min_val == val
        check_invariant(pq)


def test_from_list():
    lst = [10, 3, 5, 6, 12, 2]
    pq = priority_queue.from_list(lst)
    check_invariant(pq)
    assert lst == [10, 3, 5, 6, 12, 2]

    # Simulated test
    lst = [random.randrange(0, 100) for _ in range(100)]
    lst_ = lst.copy()
    pq = priority_queue.from_list(lst)
    check_invariant(pq)
    assert lst == lst_
    