#!/usr/bin/env python3
import asyncio
import random
"""
This module contains a type-annotated coroutine 'wait_random'
that takes in an integer argument and returns a float.
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument
    """
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
