# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2024 Hogeschool Utrecht
David Isaacs Paternostro en Tijmen Muller (tijmen.muller@hu.nl)
"""

import random
import priority_list


def test_push():
    pl = [2, 6, 3, 10, 12, 5]
    priority_list.push(pl, 1)
    assert pl == [2, 6, 3, 10, 12, 5, 1]

    # Simulated test
    for v in random.choices(range(100), k=100):
        priority_list.push(pl, v)
        assert pl[-1] == v


def test_pop():
    pl = [2, 6, 3, 10, 12, 5]

    v = priority_list.pop(pl)
    assert v == 2
    assert pl == [6, 3, 10, 12, 5]

    v = priority_list.pop(pl)
    assert v == 3
    assert pl == [6, 10, 12, 5]

    v = priority_list.pop(pl)
    assert v == 5
    assert pl == [6, 10, 12]

    v = priority_list.pop(pl)
    assert v == 6
    assert pl == [10, 12]

    v = priority_list.pop(pl)
    assert v == 10
    assert pl == [12]

    v = priority_list.pop(pl)
    assert v == 12
    assert pl == []

    v = priority_list.pop(pl)
    assert v is None
    assert pl == []
