"""

    Term

  A term is the "unique existence" attached with any symbol.

  # [TODO] make more rigorous

  Intuitively, this contrats with a symbol's semantics, which are defined by
  the *system that includes the symbol as a signifier*.

"""

from abc import ABCMeta

__all__ = [
    "Term",
]


class Term:
    __metaclass__ = ABCMeta
