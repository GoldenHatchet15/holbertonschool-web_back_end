#!/usr/bin/env python3
"""
This module contains a type-annotated function 'wait_random'
"""
import asyncio
import random


async def wait_random(max_delay: int) -> float:
    """Wait for a random delay and return the delay time."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> list:
    """Spawn wait_random n times with the specified max_delay and return sorted list of delays."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed_delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        completed_delays.append(delay)
    return completed_delays
