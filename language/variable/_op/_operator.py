"""

    *Variable Operator*

  Operate a variable.

"""

from abc import ABCMeta

from language.operator import Operator

__all__ = ["VariableOperator"]


class VariableOperator(
    Operator,
):
    __metaclass__ = ABCMeta
