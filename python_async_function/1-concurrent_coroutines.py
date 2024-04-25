#!/usr/bin/env python3
'''
Async coroutine that executes multiple coroutines at the same time
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple coroutines at the same time with async.
    """
    delays = []

    async def add_delay(delay: float):
        delays.append(delay)

    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        await task

    return sorted(delays)
