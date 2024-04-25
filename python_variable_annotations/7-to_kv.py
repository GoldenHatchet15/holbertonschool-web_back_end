#!/usr/bin/env python3
"""
This module contains a type-annotated function 'to_kv'
that takes a string and
either an int or a float and
returns a tuple with the string and
the square of the number as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and either an int or a float v
    as arguments and returns a tuple.
    """
    return (k, float(v ** 2))
