__all__ = ["AbstractAritiedOperator"]

"""

An abstract operator kinded by arity.

"""

from abc import ABCMeta
from typing import TypeVar

from language._abstract.operator import AbstractOperator


class AbstractAritiedOperator(AbstractOperator):

    __metaclass__ = ABCMeta

    Nullary = TypeVar("Nullary")
    Unary = TypeVar("Unary")
    Binary = TypeVar("Binary")
    Ternary = TypeVar("Ternary")
    Variadic = TypeVar("Variadic")
