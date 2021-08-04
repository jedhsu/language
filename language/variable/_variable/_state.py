"""

    *Variable State*

"""

from abc import ABCMeta
from dataclasses import dataclass

from language.type import Expression
from language.type import State


@dataclass
class Variable(
    State,
):
    __metaclass__ = ABCMeta

    expression: Expression
    type: Type
