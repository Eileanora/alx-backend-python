#!/usr/bin/env python3
'''This module contains function make_multiplier'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns a function that multiplies a float by multiplier'''
    def multiply_float(n: float) -> float:
        '''Returns the product of n and multiplier'''
        return n * multiplier
    return multiply_float
