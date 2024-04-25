#!/usr/bin/env python3
"""
This module contains a type-annotated function 'make_multiplier'
that takes a float multiplier and returns a function that multiplies
any float by this multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies any float by the given multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
