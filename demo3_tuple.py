from typing import Tuple


def f(t: Tuple[int, str]):
    return t[1] * t[0]


print(f((1, "pizza")))
print(f((1, 5)))
