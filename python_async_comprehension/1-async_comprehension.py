#!/usr/bin/env python3
"""
This module contains a type-annotated coroutine 'async_comprehension'
"""
from typing import List
from asyncio import sleep
from random import uniform


async def async_generator() -> float:
    """Coroutine that generates 10 random numbers asynchronously."""
    for _ in range(10):
        await sleep(1)  # Asynchronously wait for 1 second
        yield uniform(0, 10)  # Yield a random float between 0 and 10


async def async_comprehension() -> List[float]:
    """Coroutine that collects 10 random numbers using async comprehension."""
    return [num async for num in async_generator()]  # Use async comprehension to collect random numbers


