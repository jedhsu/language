"""

Bounded Polymorphic Type

A bounded polymorphic type imposes an upper type bound on the type poset.

"""

from dataclasses import dataclass

__all__ = ["ConstrainedGenericType"]

from wich._abstract.ident import AbstractNameIdent


@dataclass
class ConstrainedGenericType:
    ident: AbstractNameIdent
    # [TODO] replace with type once language model done
    bound: AbstractNameIdent
