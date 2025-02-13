# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2024 Hogeschool Utrecht
David Isaacs Paternostro en Tijmen Muller (tijmen.muller@hu.nl)
"""


import heapq
import time
import timeit
import random

import priority_list
import priority_queue


def sim_heapq_push(episodes, ns):
    print(f"\nSimulation of heapq.heappush()")
    print(f"{'n':>8}\t{"mean duration":>13}")

    for n in ns:
        # Create a queue with `n` priorities
        queue = [v for v in range(100) for _ in range(n // 100)]
        heapq.heapify(queue)
        assert len(queue) == n

        # Time function
        time.sleep(1e-2)
        duration = timeit.timeit(lambda: heapq.heappush(queue, random.randrange(1, 100)), number=episodes)

        print(f"{n:8}\t{duration * 10e9 / episodes:10.0f} ns")


def sim_heapq_pop(episodes, ns):
    print(f"\nSimulation of heapq.heappop()")
    print(f"{'n':>8}\t{"mean duration":>13}")

    for n in ns:
        # Create a queue with `n` priorities
        queue = [v for v in range(100) for _ in range(n // 100)]
        heapq.heapify(queue)
        assert len(queue) == n

        # Time function
        time.sleep(1e-2)
        duration = timeit.timeit(lambda: heapq.heappop(queue), number=episodes)

        print(f"{n:8}\t{duration * 10e9 / episodes:10.0f} ns")


def sim_plist_push(episodes, ns):
    print(f"\nSimulation of priority_list.push()")
    print(f"{'n':>8}\t{"mean duration":>13}")

    for n in ns:
        # Create a queue with `n` priorities
        lst = [random.randrange(0, 100) for _ in range(n)]
        assert len(lst) == n

        # Only simulate if implemented
        if priority_list.push(lst, 0) is None:
            print("\tFunction not implemented")
        else:
            # Time function
            time.sleep(1e-2)
            duration = timeit.timeit(lambda: priority_list.push(lst, random.randrange(1, 100)), number=episodes)

            print(f"{n:8}\t{duration * 10e9 / episodes:10.0f} ns")


def sim_plist_pop(episodes, ns):
    print(f"\nSimulation of priority_list.pop()")
    print(f"{'n':>8}\t{"mean duration":>13}")

    for n in ns:
        # Create a queue with `n` priorities
        lst = [random.randrange(0, 100) for _ in range(n)]
        assert len(lst) == n

        # Only simulate if implemented
        if priority_list.pop(lst) is None:
            print("\tFunction not implemented")
        else:
            # Time function
            time.sleep(1e-2)
            duration = timeit.timeit(lambda: priority_list.pop(lst), number=episodes)

            print(f"{n:8}\t{duration * 10e9 / episodes:10.0f} ns")


def sim_pqueue_push(episodes, ns):
    print(f"\nSimulation of priority_queue.push()")
    print(f"{'n':>8}\t{"mean duration":>13}")

    for n in ns:

        # Create a queue with `n` priorities
        queue = [v for v in range(100) for _ in range(n // 100)]
        heapq.heapify(queue)
        assert len(queue) == n

        # Only simulate if implemented
        if priority_queue.push(queue, 0) is None:
            print("\tFunction not implemented")
        else:
            # Time function
            time.sleep(1e-2)
            duration = timeit.timeit(lambda: priority_queue.push(queue, random.randrange(1, 100)), number=episodes)

            print(f"{n:8}\t{duration * 10e9 / episodes:10.0f} ns")


def sim_pqueue_pop(episodes, ns):
    print(f"\nSimulation of priority_queue.pop()")
    print(f"{'n':>8}\t{"mean duration":>13}")

    for n in ns:
        # Create a queue with `n` priorities
        queue = [v for v in range(100) for _ in range(n // 100)]
        heapq.heapify(queue)
        assert len(queue) == n

        # Only simulate if implemented
        if priority_queue.pop(queue) is None:
            print("\tFunction not implemented")
        else:
            # Time function
            time.sleep(1e-2)
            duration = timeit.timeit(lambda: priority_queue.pop(queue), number=episodes)

            print(f"{n:8}\t{duration * 10e9 / episodes:10.0f} ns")


if __name__ == '__main__':
    # Note: not a completely fair simulaton, as the heap/list grows from n to n + episodes in size
    eps = 10_000
    sizes = [1_000_000 * 2 ** i for i in range(6)]
    print(eps, 'episodes times problem size `n`:', sizes)

    time.sleep(.1)
    sim_start = time.time()

    sim_heapq_push(eps, sizes)
    sim_heapq_pop(eps, sizes)

    sim_plist_push(eps, sizes)
    sim_plist_pop(eps, [size // 1000 for size in sizes])

    sim_pqueue_push(eps, sizes)
    sim_pqueue_pop(eps, sizes)

    print(f"\n\nSimulation done after {time.time() - sim_start:.2f} s")
