#!/usr/bin/env python3
'''This module contains the fuction async_generator'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Function that yeilds a random number every 1 sec'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
