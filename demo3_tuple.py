from typing import Tuple

def f(t: Tuple[int, str]):
    return t[1] * t[0]

f((1, "pizza"))
f((1, 5))
