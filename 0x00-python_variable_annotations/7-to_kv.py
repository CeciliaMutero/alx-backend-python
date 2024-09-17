#!/usr/bin/env python3


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """Return a tuple where the first element is a
    string and the second is the square of v as a float."""
    return (k, float(v ** 2))
