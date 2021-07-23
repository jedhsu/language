"""

    *Incoherent*

  Incoherent, logically-speaking.

"""

from abc import ABCMeta

from .._logical import Logical

__all__ = ["Incoherent"]


class Incoherent(
    Logical,
):
    __metaclass__ = ABCMeta
