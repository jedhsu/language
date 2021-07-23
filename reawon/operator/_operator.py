__all__ = ["AbstractOperator"]

"""

An abstract operator.

"""

from abc import ABCMeta
from typing import TypeVar, Generic

from ..type.type import AbstractType
from ..type.type import DummyAbstractOperator

S = TypeVar("S", bound=AbstractType)
T = TypeVar("T", bound=AbstractType)


class AbstractOperator(
    DummyAbstractOperator,
    Generic[S, T],
):
    __metaclass__ = ABCMeta

    input: S
    output: T


S1 = TypeVar("S0", bound=AbstractFirstKind)
T1 = TypeVar("T0", bound=AbstractFirstKind)


class AbstractFirstKindOperator(
    DummyAbstractOperator,
    Generic[S1, T1],
):
    __metaclass__ = ABCMeta
    input: S1
    output: T1


# [TODO] kind 2 operator...
