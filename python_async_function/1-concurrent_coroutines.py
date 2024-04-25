#!/usr/bin/env python3
'''
Coroutine that spawns wait_random multiple times concurrently and returns
the list of delays in ascending order based on completion.
'''
import asyncio
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Spawns wait_random n times with the specified max_delay. Returns the list
    of all the delays (float values) in ascending order as they complete.
    
    Args:
    n (int): The number of times to spawn wait_random.
    max_delay (int): The maximum delay for wait_random.
    
    Returns:
    list: Delays in ascending order of completion.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays

if __name__ == "__main__":
    # Testing the function with different inputs
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
