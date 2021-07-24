"""

Syntax expression operators.

"""

from typing import Sequence


class _Operator:
    Sequence = "-"
    OrderedChoice = "/"
    ZeroOrMore = "*"
    OneOrMore = "+"
    Optional = "?"
    And = "&"


class Precedence(_Operator):
    @classmethod
    def precedence(cls) -> Sequence[str]:
        return [
            cls.Sequence,
            cls.OrderedChoice,
            cls.ZeroOrMore,
            cls.OneOrMore,
            cls.Optional,
            cls.And,
        ]
