"""

    *Thing*

  Things are vague, intuitionistic, and imprecise.

  By using intuition, you can extend thing but cannot add methods,
  mimicking how the actual metaprocess is.

  A thing can be coherent, therefore something can be coherent and vague.

"""

from abc import ABCMeta

from .vague import vague

__all__ = ["Thing"]


@vague
class Thing:
    __metaclass__ = ABCMeta
