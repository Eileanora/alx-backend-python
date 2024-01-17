#!/usr/bin/env python3
'''This module contains the function measure_runtime'''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures the total runtime and returns it'''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time.time()
    return end_time - start_time
