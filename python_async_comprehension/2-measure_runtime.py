#!/usr/bin/env python3
import asyncio
from time import perf_counter
from typing import List


async def measure_runtime() -> float:
    """Measure the total runtime of executing async_comprehension four times in parallel."""
    start_time = perf_counter()  # Record the start time

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = perf_counter()  # Record the end time

    # Calculate the total runtime
    total_runtime = end_time - start_time
    return total_runtime
