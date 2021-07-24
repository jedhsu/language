"""

Syntax Expression.

"""

# [TODO] rename to Form?

from __future__ import annotations
from dataclasses import dataclass

from ..symbol.symbol import Symbol

__all__ = [
    # "Expr",
    "Atom",
    "Seq",
    "Choice",
    "ZeroOrMore",
    "OneOrMore",
    "Option",
    "ForwardIs",
    "ForwardNot",
]


class _Expr:
    _expr: _Expr


class _Op_(_Expr):
    def sequence(self: _Expr, expr: _Expr) -> _Expr:
        """Operator is  -  ."""
        return Seq(self, expr)

    # def choice(self: _Expr, expr2: _Expr) -> _Expr:
    #     return Choice(self, expr2)

    def zero_or_more(self: _Expr) -> _Expr:
        return ZeroOrMore(self)

    def one_or_more(self: _Expr) -> _Expr:
        return OneOrMore(self)

    def __getitem__(self, slc: slice) -> _Expr:
        if slc == slice(0, None, None):
            return self.zero_or_more()
        elif slc == slice(1, None, None):
            return self.one_or_more()
        else:
            raise SyntaxError("Unallowed syntax.")

    def option(self: _Expr) -> _Expr:
        return Option(self)


#     def and_(self: _Expr) -> _Expr:
#         return And_(self)

#     def not_(self: _Expr) -> _Expr:
#         return Not_(self)


class _OpSign_(_Op_):
    def __sub__(self, expr: _Expr) -> _Expr:
        return self.sequence(expr)


class _Expr_(_Op_, _Expr):
    _expr: _Expr


"""

Oi can do three things:

1. Expand
2. Reduce
3. Abstract

Envision what each operation does to the tree.

"""


# TODO: generalize this container is a type of itself concept later!
# Oi

# Expansion
# Reduction

# class Expand:
#     o:
#     i


@dataclass
class Atom(_Expr_):
    expr: Symbol


@dataclass
class Seq(_Expr_):
    expr1: _Expr
    expr2: _Expr

    def seq1(self) -> bool:
        return isinstance(self.expr1, Seq)

    def seq2(self) -> bool:
        return isinstance(self.expr2, Seq)

    def __repr__(self):
        if isinstance(self.expr1, Seq) and isinstance(self.expr2, Seq):
            lines = [
                f"Seq[",
                f"    {self.expr1.expr1}",
                f"    {self.expr1.expr2}",
                f"    {self.expr2.expr2}",
                f"    {self.expr2.expr2}",
                f"]",
            ]

    @classmethod
    def __class_getitem__(cls, kv: tuple[_Expr, _Expr]):
        return cls(*kv)

    @staticmethod
    def __compose__(expr1: _Expr, expr2: _Expr) -> _Expr:
        return Seq(expr1, expr2)


@dataclass
class Choice(_Expr_):
    expr1: _Expr
    expr2: _Expr


@dataclass
class ZeroOrMore(_Expr_):
    expr: _Expr


@dataclass
class OneOrMore(_Expr_):
    expr: _Expr


@dataclass
class Option(_Expr_):
    expr: _Expr

    @classmethod
    def __class_getitem__(cls, expr: _Expr):
        return cls(expr)


@dataclass
class ForwardIs(_Expr_):
    """Positive lookahead."""

    expr: _Expr
    forward_expr: _Expr

    @classmethod
    def __class_getitem__(cls, kv: tuple[_Expr, _Expr]):
        return cls(*kv)

    @staticmethod
    def __compose__(expr1: _Expr, expr2: _Expr) -> _Expr:
        return Seq(expr1, expr2)


@dataclass
class ForwardNot(_Expr_):
    expr: _Expr
    forward_expr: _Expr

    @classmethod
    def __class_getitem__(cls, kv: tuple[_Expr, _Expr]):
        return cls(*kv)


# class Expr(_Expr, Atom):
#     def __init__(self, expr: _Expr):
#         self._expr = expr
