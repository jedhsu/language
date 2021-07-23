"""

    *Property*

  I think property is a good example here. It is pretty clearly not a trait, but
  rather some structural associated thing.

"""

from abc import ABCMeta

from wich.__intuition import Intuitive
from ._structure import Structure


__all__ = ["Property"]


class Property(
    Structure,
    Intuitive,
):
    __metaclass__ = ABCMeta
