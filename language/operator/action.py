"""

    *Action*   i.e. *Monad*

  An operator which returns a type and an effect.

"""

from abc import ABCMeta

from ._operator import Operator

__all__ = ["Action"]


class Action(
    Operator,
):
    __metaclass__ = ABCMeta
