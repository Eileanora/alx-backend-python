#!/usr/bin/env python3
'''This module contains the function safely_get_value'''
from typing import Mapping, Any, Union, TypeVar


def safely_get_value(dct: Mapping, key: Any,
                     default:
                     Union[TypeVar('T'), None]) -> Union[Any, TypeVar('T')]:
    '''Returns the value of a key in a dictionary'''
    if key in dct:
        return dct[key]
    else:
        return default
