from ..seq import Seq
from ..symbol import Symbol


class TestSeq:
    def test_seq(self):
        seq = Seq("1", Symbol("2"), "3")

        assert seq == ("1", Symbol("2"), "3")
