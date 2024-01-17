#!/usr/bin/env python3
'''This module contains the function wait_n'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''This function returns the list of all the delays (float values).'''
    tasks: List[float] = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    return sorted([await task for task in asyncio.as_completed(tasks)])
