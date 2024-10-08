#!/usr/bin/env python3
"""
Takes a float multiplier as argument and
returns a function that
multiplies a float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""
    def multiplier_function(x: float) -> float:
        """Multiplies the given float `x` by the `multiplier`."""
        return x * multiplier
    return multiplier_function
