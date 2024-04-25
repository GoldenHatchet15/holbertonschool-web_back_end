#!/usr/bin/env python3
"""
Test file for printing the correct output of the wait_n coroutine
"""
import asyncio
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Spawns wait_random n times with the specified max_delay.
    Collects and returns the list of all delays (float values) 
    as they finish.
    
    Args:
    n (int): Number of concurrent calls to wait_random.
    max_delay (int): Maximum delay value for wait_random.
    
    Returns:
    list: Delays collected in the order of completion.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_delays = []
    for future in asyncio.as_completed(tasks):
        result = await future
        completed_delays.append(result)
    return completed_delays

if __name__ == "__main__":
    # Ensure your main testing logic here
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
