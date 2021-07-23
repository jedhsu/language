from enum import Enum
from typing import Literal as _Literal, Sequence

from .lexeme import Lexeme

__all__ = ["Token"]

# backwards / forwards paradox again...

# TODO: improve on this
Type = type
Object = object  # TODO: make this precise


def construct(name, bases: Sequence[Type]):
    ...


def create(name, bases: Sequence[Type], methods) -> Object:
    ...


class _Token(Enum):
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"


class Line(int):
    ...


class Literal(Enum, _Literal):
    ...


class TokenType:
    ...


class Token(
    type,
    Lexeme,
    Literal,
    Line,
):
    ...


def scan():
    ...
