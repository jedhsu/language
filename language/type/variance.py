"""

    *Type Variance*

  The type variance relations.

"""

from .type import AbstractType


class TypeVariance(
    AbstractType,
):
    def is_covariant_to(self) -> bool:
        self.function(input) <= self.function(output)

    def contravariant(self) -> bool:
        self.function(output) <= self.function(input)

    def invariant(self) -> bool:
        pass
