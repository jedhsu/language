from abc import ABCMeta

from .abstract import AbstractVariable

__all__ = ["MetaVariable"]


class MetaVariable(AbstractVariable):

    __metaclass__ = ABCMeta

    pass
