#!/usr/bin/env python3
"""
This module contains an asynchronous generator that yields 10 random numbers,
each between 0 and 10, with a one-second delay between each yield.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generate ten random numbers between 0 and 10, each followed
    by a one-second delay. Yields a float for each number generated.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
