#!/usr/bin/env python3
'''This module contains the function async_comprehension'''
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    '''Collects 10 rand numbers from asyc generator and returns them'''
    results = [i async for i in async_generator()]
    return results
