#!/usr/bin/env python3
"""
Computes the length of each sequence in the given iterable.
"""


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each sequence in the given iterable.
    """
    return [(i, len(i)) for i in lst]