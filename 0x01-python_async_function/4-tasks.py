#!/usr/bin/env python3
'''This module contains the function task_wait_random'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Call task wait random and return the list of all delays'''
    tasks: List[float] = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))

    return sorted([await task for task in asyncio.as_completed(tasks)])
