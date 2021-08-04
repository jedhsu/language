"""

    *Declare*

  Binds a _type_ to a variable.

"""

from abc import ABCMeta

from ._operator import VariableOperator

__all__ = ["Declare"]


class Declare(
    VariableOperator,
):
    __metaclass__ = ABCMeta
