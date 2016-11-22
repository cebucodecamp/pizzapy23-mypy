reveal_type(len("blub"))


def get_id(name: str):
    return len(name)

reveal_type(get_id("blub"))


# limitations_inference.py:1: error: Revealed type is 'builtins.int'
# limitations_inference.py:7: error: Revealed type is 'Any'
