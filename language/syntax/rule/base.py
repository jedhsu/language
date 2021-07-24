from abc import ABCMeta
from dataclasses import dataclass

from ..form import Form

__all__ = ["AbstractRule"]

"""

Abstract Rule

Represents the infinite set of *concrete rules* obtained by replacing each
metavariable from the appropriate syntactic category.

"""


class Satisfy:
    def satisfied(rel: Relation):
        pass


@dataclass
class AbstractRule(metaclass=ABCMeta):
    left: Form
    right: Form

    def generate_set(self):
        """

        Define the left and right as statement.


        """
        # ref[Pierce-27]

        pass


class _Display_(_Rule):
    def __repr__(self):
        return f"{self.given}  -->  {self.thus}"


class Judgment:
    def derivable(self):
        pass


class Term:
    def normal(self):
        pass


class Value(Normal):
    pass
