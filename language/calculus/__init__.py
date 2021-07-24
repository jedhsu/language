"""

Lambda calculus base model.

"""


from abc import ABCMeta
from dataclasses import dataclass


"""

Verify that alpha equivalence is an isomorphism.

"""


class Term(metaclass=ABCMeta):
    def is_closed(self):
        pass


class Variable(Term, str):
    def __init__(self, identifier: str):
        super(Variable, self).__new__(str, identifier)

    def is_free(self):
        pass

    def is_bound(self):
        pass


@dataclass
class Application(Term):
    left: Term
    right: Term


class Precedence:
    pass


class Associativity:
    pass
