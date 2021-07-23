from dataclasses import dataclass
from typing import Any

from ..term import Term
from ..variable import Variable

__all__ = ["Abstraction"]


class AnonymousRepresentation:
    """
    Implementation of De Bruijn indexation scheme.

    """


@dataclass
class _Abstraction:
    head: Variable
    body: Term


class _Display_(_Abstraction):
    symbol = "\u25b9"

    def __repr__(self) -> str:
        return f"{self.symbol}{self.head}.{self.body}"


class Binder:
    body: Any  # [TODO] precise typing

    def scope(self):
        return self.body


@dataclass
class Abstraction(
    AnonymousRepresentation,
    Binder,
    _Display_,
    Term,
):
    variable: Variable
    body: Term

    def bind(self, var: Variable):
        pass

    def nameless_index(self):
        pass

    def shift(self):
        pass

    def substitute(self):
        pass
