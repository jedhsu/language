from ..symbol import Symbol


class TestSymbol:
    def test_init(self):
        A = Symbol("A")

        assert isinstance(A, Symbol)


class TestDefault:
    def test_A(self):
        A = Symbol.A()
        assert A == Symbol("A")


class TestCompose:
    def test_add(self):
        assert Symbol("A") + Symbol("B") == Symbol("AB")


class TestDisplay:
    def test_repr(self):
        assert repr(Symbol("A")) == "A"
