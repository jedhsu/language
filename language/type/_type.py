"""

    *Type Ideal*

  A theoretical type makes the idea of a type precise.



"""

from abc import ABCMeta

__all__ = ["TypeIdeal"]


class TypeIdeal(
    Theory,
    TypeSemantics,
):
    __metaclass__ = ABCMeta
