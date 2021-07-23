"""
Parsing Expression Grammar.
"""

from .symbol import NonTerminalSymbol, TerminalSymbol

__all__ = ["Peg"]


class _Peg_:
    N: set[NonTerminalSymbol]
    Sigma: set[TerminalSymbol]


class Peg:
    ...
