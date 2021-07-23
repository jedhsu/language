"""

    *Abstract Type*

  A type is defined by a collection of values, and a collection of operators
  defined on these values.

  The "very" uncountable size of values is one part that makes this tricky.

"""

from typing import Any
from abc import ABCMeta

__all__ = ["AbstractType"]

from ..collection import AbstractCollection

# [TODO] fixing chicken and egg problem with quick solution, deal with it later
class DummyAbstractOperator:
    __metaclass__ = ABCMeta
    pass


class AbstractType:
    __metaclass__ = ABCMeta

    values: AbstractCollection[Any]
    operators: set[DummyAbstractOperator]
