"""

    *Structure*

"""

from abc import ABCMeta

from wich.__core._thing import Thing
from wich.__intuition import Intuitive

__all__ = ["Structure"]


class Structure(
    Thing,
    Intuitive,
):
    __metaclass__ = ABCMeta
