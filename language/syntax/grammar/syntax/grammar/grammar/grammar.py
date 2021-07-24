from collections.abc import Collection
from typing import Literal, Sequence

from .rule import Rule

Terminal = Literal


class Alphabet(Sequence[Terminal]):
    ...


class Grammar(Alphabet, Collection[Rule]):
    ...
