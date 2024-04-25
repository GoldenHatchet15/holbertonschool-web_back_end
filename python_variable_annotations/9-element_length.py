#!/usr/bin/env python3
"""
This module contains a type-annotated function 'element_length'
that returns a list of tuples, each containing an item from the input
iterable and the length of that item.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    """
    return [(i, len(i)) for i in lst]
