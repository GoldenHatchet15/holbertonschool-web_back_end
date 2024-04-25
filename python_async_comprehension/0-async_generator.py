#!/usr/bin/env python3
"""
This module contains an async generator 'async_generator'
that generates 10 random numbers between 0 and 10.
"""
import asyncio
import random


async def async_generator():
    """
    Asynchronously generates 10 random numbers between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)