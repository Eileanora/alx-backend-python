#!/usr/bin/env python3
'''Module for the function async_generator'''
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Generator that yields a random number between 0 and 10 every 1 second'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
