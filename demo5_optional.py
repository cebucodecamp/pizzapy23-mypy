from typing import Any, Optional


def f():
    return None


def g() -> Any:
    return None


def h(a) -> Optional[int]:
    if a:
        return None
    return 3


def i(a) -> int:
    if a:
        return None  # fails with --strict-optional
    return 3
