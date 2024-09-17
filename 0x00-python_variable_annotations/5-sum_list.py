#!/usr/bin/env python3
"""module that akes a list input_list of
floats as argument and
returns their sum as a float"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats."""
    sum: float = 0.0
    for num in input_list:
        sum += num
    return sum
