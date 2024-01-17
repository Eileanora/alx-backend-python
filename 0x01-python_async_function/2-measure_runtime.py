#!/usr/bin/env python3
'''This module contains the function measure_runtime'''
import asyncio
import time
from typing import List, Tuple


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''This function measures the total execution time for wait_n'''
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    return (end_time - start_time) / n
