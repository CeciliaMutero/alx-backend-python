#!/usr/bin/env python3
"""
Takes a string k and an int OR float v
as arguments and returns a tuple.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """Return a tuple where the first element is a
    string and the second is the square of v as a float."""
    square = v ** 2
    return (k, int(square) if isinstance(v, int) else float(square))
