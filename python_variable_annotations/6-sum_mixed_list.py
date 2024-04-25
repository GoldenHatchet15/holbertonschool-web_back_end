#!/usr/bin/env python3
"""
This module contains a type-annotated function 'sum_mixed_list'
that sums a list of integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing both integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
    float: The sum of the list elements, as a float.
    """
    return float(sum(mxd_lst))
