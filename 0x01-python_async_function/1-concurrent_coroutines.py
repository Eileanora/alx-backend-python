#!/usr/bin/env python3
"""Module for task_wait_n"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that returns the list of all the delays"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
