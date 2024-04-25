#!/usr/bin/env python3
'''
Coroutine that spawns wait_random multiple times concurrently and returns
the list of delays in ascending order based on completion.
'''
import asyncio
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> list:

    '''
    Spawns wait_random n times with max_delay
    '''
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
