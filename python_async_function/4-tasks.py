#!/usr/bin/env python3
"""
Defines a function task_wait_n to create asyncio.Tasks.
"""

import asyncio
from typing import List
from asyncio import Task

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    Parameters:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay value for task_wait_random.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
