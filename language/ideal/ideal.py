"""

    *Ideal*

  The ideal of a thing.

  It's not a paradox! It's EMERGENT!

  there is no chicken-egg problem.

  But there is B(A) ==> C(B(A)).

  It this at all less illogical? ugh lol.

  You can only develop A through B. But by developing B,
  A becomes C as well.

  Everythign so far is intuitive. THeories improve our truth and understanding in some objective way,
  though the thing can remain ambiguous.

  Ideals are the implementation of that objective part of truth.

"""

__all__ = ["Ideal"]

from abc import ABCMeta

from .theory import Theory
from .thing import Thing


class Ideal(
    Logical,
    Coherent,
    Theory,
    Thing,
):
    __metaclass__ = ABCMeta
