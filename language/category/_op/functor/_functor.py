"""

Abstract Functor

A functor is an operator defined on a type that consists of mappings from objects,
and mappings for a morphism.

i.e. contains a Transform type and Morphism type
"""

from typing import TypeVar, Generic

__all__ = ["AbstractFunctor"]

from ..type import AbstractType
from ._operator import AbstractOperator

from .core.transform import AbstractTransform
from .core.morphism import AbstractMorphism

C = TypeVar("C", bound=AbstractType)

# [TODO] need to do the class getitem trick

"""
this is known as AbstractFunctor[C, D]
makes sense as the functor category / functor type.
"""


class AbstractFunctor(
    AbstractOperator,
):
    transforms: set[AbstractTransform[C, D]]
    morphisms: set[AbstractMorphism[C]]  # one morphism for every AbstractMorphism[C]
