from abc import ABCMeta

__all__ = ["AbstractVariable"]


class AbstractVariable(str):

    __metaclass__ = ABCMeta

    def __init__(self, symbol: str):
        return super(AbstractVariable, self).__new__(str, symbol)
