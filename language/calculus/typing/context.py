"""

Typing context.     Γ

Set of assumptions about the types of the free variables of T.

"""

from ...typing import Sequence, TypeDeclaration
from ..variable import Variable


class _Display_:
    symbol = "Gamma"

    def __repr__(self):
        pass


@dataclass
class TypingContext(set[TypeDeclaration]):
    def rule(self):
        # [TODO] how do we program this?
        return Add(Variable, Sequence[Variable])

    def domain(self) -> set[Variable]:
        """
        The set of variables bound by the typing context.

        """
