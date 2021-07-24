"""
    
    *Abstract Type Of*

    In a way, a type is a fixed mapping.

  Return an explicitly bound type.

"""

from abc import ABCMeta

from ._operator import AbstractTypedVariableOperator

__all__ = ["AbstractTypeOf"]


class AbstractTypeOf(
    AbstractTypedVariableOperator,
):
    __metaclass__ = ABCMeta
