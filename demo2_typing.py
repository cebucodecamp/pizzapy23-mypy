from typing import List
# ./runmypy cat /usr/local/lib/python3.6/typing.py


def count_plus_first(it: List[int]):
    return len(it) + it[0]


print(count_plus_first(list(range(10))))
