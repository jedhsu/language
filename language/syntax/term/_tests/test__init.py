from ..form import Form, Term


def test_behavior():
    assert type(Term) == Form, type(Term)
    assert issubclass(Term, Form)


class TestTerm:
    pass


# class TestForm:
#     def test_parents(self):
#         assert Form.__bases__ is None, Form.__bases__
