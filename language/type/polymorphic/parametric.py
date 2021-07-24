"""

Parametric Polymorphic Type

A parametric polymorphic type can range over any type in a type heirarchy.

"""

from dataclasses import dataclass

__all__ = ["PolymorphicType"]

from wich._ident import AbstractNameIdent


@dataclass
class ParametricPolymorphicType(
    PolymorphicType,
):
    ident: AbstractNameIdent
