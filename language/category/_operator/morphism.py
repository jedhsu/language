"""

Abstract Morphism

A morphism is an operator that maps a type to itself.

The notation AbstractMorphism[C] thus makes sense.

"""

from typing import TypeVar, Generic

__all__ = ["AbstractMorphism"]

from .._operator import AbstractOperator
from ...type import AbstractType

C = TypeVar("C", bound=AbstractType)

# WORK ON SOME GEOMETRIC INTUITION TO MAKE THIS CLEAR!


class AbstractMorphism(
    AbstractOperator,
    Generic[C],
):
    input: C
    output: C
