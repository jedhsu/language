from ..term import Term
from .abstract import AbstractVariable


class Variable(Term, AbstractVariable):
    def __init__(self, identifier: str):
        super(Variable, self).__new__(str, identifier)

    def is_free(self):
        pass

    def is_bound(self):
        pass
