"""

    *Polymorphic Type*

  A polymorphic type is a type containg a set of types.

"""

# [TODO} check def - clarify


from abc import ABCMeta
from dataclasses import dataclass

__all__ = [
    "PolymorphicType",
]


@dataclass
def PolymorphicType(
    Type,
):
    __metaclass__ = ABCMeta

    types: set[Type]
