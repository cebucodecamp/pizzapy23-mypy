from typing import Text, Union


class FakeResponse(object):
    def jsom(self) -> None: ...


def get(url: Text, **kwargs) -> FakeResponse: ...
