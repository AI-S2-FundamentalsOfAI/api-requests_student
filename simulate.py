# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2024 Hogeschool Utrecht
David Isaacs Paternostro en Tijmen Muller (tijmen.muller@hu.nl)
"""


import heapq
import time
import numpy as np
import random

import priority_list
import priority_queue


def sim_heapq_push(episodes, ns):
    print(f"\nSimulation of heapq.heappush()")
    print(f"{'n':>6}\t{"mean duration":>13}")

    for n in ns:
        duration = 0
        for _ in range(episodes):
            # Create a queue with `n` priorities
            queue = [v for v in range(100) for _ in range(n // 100)]
            heapq.heapify(queue)
            assert len(queue) == n

            # Time function
            start = time.process_time_ns()
            heapq.heappush(queue, random.randrange(1, 100))
            duration += time.process_time_ns() - start

        print(f"{n:6}\t{duration / episodes:10.0f} ns")


def sim_heapq_pop(episodes, ns):
    print(f"\nSimulation of heapq.heappop()")
    print(f"{'n':>6}\t{"mean duration":>13}")

    for n in ns:
        duration = 0
        for _ in range(episodes):
            # Create a queue with `n` priorities
            queue = [v for v in range(100) for _ in range(n // 100)]
            heapq.heapify(queue)
            assert len(queue) == n

            # Time function
            start = time.process_time_ns()
            heapq.heappop(queue)
            duration += time.process_time_ns() - start

        print(f"{n:6}\t{duration / episodes:10.0f} ns")


def sim_plist_push(episodes, ns):
    print(f"\nSimulation of priority_list.push()")
    print(f"{'n':>6}\t{"mean duration":>13}")

    for n in ns:
        duration = 0
        for _ in range(episodes):
            # Create a queue with `n` priorities
            lst = [random.randrange(0, 100) for _ in range(n)]
            assert len(lst) == n

            # Time function
            start = time.process_time_ns()
            priority_list.push(lst, random.randrange(1, 100))
            duration += time.process_time_ns() - start

        print(f"{n:6}\t{duration / episodes:10.0f} ns")


def sim_plist_pop(episodes, ns):
    print(f"\nSimulation of priority_list.pop()")
    print(f"{'n':>6}\t{"mean duration":>13}")

    for n in ns:
        duration = 0
        for _ in range(episodes):
            # Create a queue with `n` priorities
            lst = [random.randrange(0, 100) for _ in range(n)]
            assert len(lst) == n

            # Time function
            start = time.process_time_ns()
            priority_list.pop(lst)
            duration += time.process_time_ns() - start

        print(f"{n:6}\t{duration / episodes:10.0f} ns")


def sim_pqueue_push(episodes, ns):
    print(f"\nSimulation of priority_queue.push()")
    print(f"{'n':>6}\t{"mean duration":>13}")

    for n in ns:
        duration = 0
        for _ in range(episodes):
            # Create a queue with `n` priorities
            queue = [v for v in range(100) for _ in range(n // 100)]
            heapq.heapify(queue)
            assert len(queue) == n

            # Time function
            start = time.process_time_ns()
            priority_queue.push(queue, random.randrange(1, 100))
            duration += time.process_time_ns() - start

        print(f"{n:6}\t{duration / episodes:10.0f} ns")


def sim_pqueue_pop(episodes, ns):
    print(f"\nSimulation of priority_queue.push()")
    print(f"{'n':>6}\t{"mean duration":>13}")

    for n in ns:
        duration = 0
        for _ in range(episodes):
            # Create a queue with `n` priorities
            queue = [v for v in range(100) for _ in range(n // 100)]
            heapq.heapify(queue)
            assert len(queue) == n

            # Time function
            start = time.process_time_ns()
            priority_queue.pop(queue)
            duration += time.process_time_ns() - start

        print(f"{n:6}\t{duration / episodes:10.0f} ns")


if __name__ == '__main__':
    eps = 1_000
    sizes = [1_000 * 2 ** i for i in range(6)]
    print(eps, 'episodes times problem size `n`:', sizes)

    time.sleep(.1)
    sim_start = time.time()

    sim_heapq_push(eps, sizes)
    sim_heapq_pop(eps, sizes)

    sim_plist_push(eps, sizes)
    sim_plist_pop(eps, sizes)

    sim_pqueue_push(eps, sizes)
    sim_pqueue_pop(eps, sizes)

    print(f"Simulation done after {time.time() - sim_start:.2f} s")
