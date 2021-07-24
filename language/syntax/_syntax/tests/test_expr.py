from ...symbol.symbol import Symbol
from ..expr import Atom, ForwardIs, Option, Seq, ZeroOrMore, _Expr, _Expr_, _Op_


class Test_Op_:
    def test_sequence(self):
        ...


class TestAtom:
    def test_init(self):
        expr = Atom(Symbol("A"))

    def test_mro(self):
        expr = Atom(Symbol("A"))

        assert isinstance(expr, Atom)
        assert isinstance(expr, _Expr_)
        assert isinstance(expr, _Op_)
        assert isinstance(expr, _Expr)


class TestSeq:
    expr1 = Atom(Symbol("A"))
    expr2 = Atom(Symbol("B"))

    seq = Seq(expr1, expr2)

    def test_init(self):
        assert self.seq.expr1 == Atom(Symbol("A"))
        assert self.seq.expr2 == Atom(Symbol("B"))

    def test_class_getitem(self):
        seq = Seq[self.expr1, self.expr2]

        assert seq.expr1 == Atom(Symbol("A"))
        assert seq.expr2 == Atom(Symbol("B"))

        assert isinstance(seq, Seq)

    def test_compose(self):
        seq = Seq.__compose__(self.seq.expr1, self.seq.expr2)

        assert seq.expr1 == Atom(Symbol("A"))
        assert seq.expr2 == Atom(Symbol("B"))


class TestOption:
    expr = Atom(Symbol("A"))

    option = Option(expr)

    def test_init(self):
        assert self.option.expr == Atom(Symbol("A"))

    def test_class_getitem(self):
        option = Option[self.expr]

        assert self.option.expr == Atom(Symbol("A"))


class TestForwardIs:
    expr1 = Atom(Symbol("A"))
    expr2 = Atom(Symbol("B"))

    forward_is = ForwardIs(expr1, expr2)

    def test_init(self):
        assert self.forward_is.expr == Atom(Symbol("A"))
        assert self.forward_is.forward_expr == Atom(Symbol("B"))

    def test_class_getitem(self):
        forward_is = ForwardIs[self.expr1, self.expr2]

        assert forward_is.expr == Atom(Symbol("A"))
        assert forward_is.forward_expr == Atom(Symbol("B"))

        assert isinstance(forward_is, ForwardIs)


class TestOp:
    expr = Atom(Symbol("A"))
    expr2 = Atom(Symbol("B"))

    def test_sequence(self):
        assert self.expr.sequence(self.expr2) == Seq[self.expr, self.expr2]

    def test_zero_or_more(self):
        assert self.expr.zero_or_more() == ZeroOrMore(self.expr)

    def test_zero_or_more_op(self):
        assert self.expr[0:] == ZeroOrMore(self.expr)

    def test_option(self):
        ...
