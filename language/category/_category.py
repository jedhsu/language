"""

    *Category*   C

  The category of category theory is a type where the operators are morphisms.

  The interesting things start happening when you partition by kind.
  
  # [TODO] unicode needs cursive

"""

from typing import Any


from .type import AbstractType
from .operator import AbstractMorphism


__all__ = ["Category"]

# I think category is relevant in that it can be any one of the kind levels, but that's a relevat distinction.
# because morphisms are dealing with mappings between lower and higher rank - form a equivalence rel in a way.


class Category(
    AbstractType,
):
    values: Any
    operators: AbstractMorphism
