from enum import Enum
from typing import Literal

from .rule import Rule


class _Symbol(Enum):
    Terminal = 0
    Nonterminal = 1


class Terminal(_Symbol, Literal):
    def __init__(self):
        super(Terminal, self).__new__(Enum, "Terminal")


# TODO: need to flesh out binding... skip for now
class Nonterminal(_Symbol):
    def __init__(self, ref: Rule):
        super(Nonterminal, self).__new__(Enum, "Nonterminal")
