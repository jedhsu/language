from .expr.expr import Expr
from .symbol.symbol import Symbol


class _ParsingRule:

    symbol: Symbol
    expr: Expr


class Default(_ParsingRule):
    @staticmethod
    def test():
        return ParsingRule(Symbol("A"), Expr(Symbol("A")))

    # TODO: there is a loading difficulty here! interesting
    @staticmethod
    def test_python_statements_rule():
        return ParsingRule(Symbol("statements"), Expr(OneOf(symbol)))


class Production(_ParsingRule):
    def __init__(self, symbol: Symbol, expr: Expr):
        super(ParsingRule, self).__init__(symbol, expr)
