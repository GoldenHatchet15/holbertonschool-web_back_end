#!/usr/bin/env python3
"""
Defines an asynchronous coroutine wait_random that waits for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds.

    Parameters:
        max_delay (int): The maximum delay value (default 10).

    Returns:
        float: The random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
