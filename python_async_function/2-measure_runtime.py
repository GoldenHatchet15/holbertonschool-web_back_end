#!/usr/bin/env python3
"""
Defines a function measure_time to measure
the total execution time for wait_n(n, max_delay).
"""

import time
import asyncio
from typing import List
from asyncio import Task

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay).

    Parameters:
        n (int): The number of times to run wait_n.
        max_delay (int): The maximum delay value for wait_n.

    Returns:
        float: The average time per operation.
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n
