"""

    *Type*

"""

from abc import ABCMeta

from language.operator import Operator

__all__ = ["Type"]


class Type(
    Operator,
):
    __metaclass__ = ABCMeta
