""""

    *Abstract Infer*

  Return an implicit type if possible.

"""

from abc import ABCMeta

from ._operator import AbstractTypedVariableOperator

__all__ = ["AbstractInfer"]


class AbstractInfer(
    AbstractTypedVariableOperator,
):
    __metaclass__ = ABCMeta
