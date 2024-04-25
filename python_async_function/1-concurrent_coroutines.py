#!/usr/bin/env python3
"""
Defines an async routine wait_n that spawns wait_random n times
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Parameters:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay value for wait_random.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return sorted(delays)
