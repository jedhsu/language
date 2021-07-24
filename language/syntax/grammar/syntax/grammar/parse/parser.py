from .syntax import SyntaxTree

__all__ = ["Parser"]


class Parse:
    @staticmethod
    def parse(tokens: Stream[Token]) -> SyntaxTree:
        ...


class Parser(Parse):
    ...
