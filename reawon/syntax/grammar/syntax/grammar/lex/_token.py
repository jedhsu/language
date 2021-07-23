from enum import Enum


class Character(Enum):
    left_paren = 0


class Literal(Enum):
    identifier = 0


class _Token(Character, Literal):
    ...
