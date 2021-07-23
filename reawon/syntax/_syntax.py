"""

    *Syntax*

  Can be viewed in a way as "mechanics" of a language.

"""

from abc import ABCMeta

__all__ = [
    "Syntax",
    "LanguageMechanics",
    "Syntactic",
    "LanguageMechanical",
]


class Syntax:
    __metaclass__ = ABCMeta


LanguageMechanics = Syntax


class Syntactic:
    __metaclass__ = ABCMeta


LanguageMechanical = Syntactic
