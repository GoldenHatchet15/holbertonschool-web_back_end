#!/usr/bin/env python3
"""
This module contains a type-annotated function 'floor'
that computes the floor of a float.
"""


def floor(n: float) -> int:
    """
    Returns the floor of a float n.

    Parameters:
    n (float): The float number from which the floor will be computed.

    Returns:
    int: The floor value of n.
    """
    import math
    return math.floor(n)
