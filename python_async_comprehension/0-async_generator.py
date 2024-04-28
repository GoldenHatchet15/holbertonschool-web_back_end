#!/usr/bin/env python3
"""
This module contains an async generator that generates 10 random numbers
between 0 and 10, with a 1-second wait between each.
"""

import asyncio
import random


async def async_generator():
    """
    Asynchronously generate ten random numbers
    between 0 and 10, each followed
    by a one-second delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
