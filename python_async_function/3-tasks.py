#!/usr/bin/env python3
"""
Defines a function task_wait_random to create an asyncio.Task.
"""

import asyncio
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random coroutine
    with the given max_delay.

    Parameters:
        max_delay (int): The maximum delay value for wait_random.

    Returns:
        asyncio.Task: The created task.
    """
    return asyncio.create_task(wait_random(max_delay))
