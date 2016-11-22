from typing import List


def count_plus_first(it: List[int]):
    return len(it) + it[0]


print(count_plus_first(list(range(10))))
