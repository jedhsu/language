"""

    *Relation*

"""

from abc import ABCMeta
from dataclasses import dataclass
from typing import Mapping

from wich.__variable import AbstractVariable

__all__ = ["Relation"]

# just handling specific 2-arity case first
class BinaryRelation(metaclass=ABCMeta):
    left: AbstractVariable
    right: AbstractVariable


"""

Directly embed the implies, skipping the set-theoretic foundations.

This favors intuitionistic typing. (Modal homotopy theory??)

Importantly, a function is defined by its terms, suggesting a form of
modal equivalence between the lambda calculus and its typed form??

Pretty much a heavier lambda?

FunctionDef and Operator should inherit from this base.

"""


class Input:
    """
    Variadic sequence of types.

    """

    @property
    def arity(self):
        pass


class Output:
    """
    Return type.

    """


@dataclass
class Relation(Mapping[Input, Output]):
    input: Input
    output: Output

    evaluations: Statement.Chain

    def check_well_defined():
        pass
