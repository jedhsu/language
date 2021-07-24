from ..symbol import Symbol


class TestSymbol:
    def test_init(self):
        a = Symbol("a")

        assert a == "a"
        assert isinstance(a, str)
        assert isinstance(a, Symbol)
