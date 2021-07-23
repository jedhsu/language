"""

Symbol base type.

Inherits from immutable string.

"""
from abc import ABCMeta


class _Symbol(str):
    def __init__(self, symbol: str):
        super(_Symbol, self).__new__(_Symbol, symbol)


class _Compose_(_Symbol):
    # [TODO] need to check type variance
    def __add__(self, s: _Symbol):
        return Symbol(self + s)


class _Display_(_Symbol):
    def __repr__(self):
        return self


class _Default_:
    @staticmethod
    def A():
        return Symbol("A")


class Symbol(
    _Default_,
    _Display_,
    _Compose_,
    _Symbol,
    metaclass=ABCMeta,
):
    pass
