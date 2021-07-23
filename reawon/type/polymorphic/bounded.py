"""

    Bounded Polymorphic Type

  A bounded (constrianed) polymorphic type imposes an upper type bound on the type poset.

"""

from dataclasses import dataclass

__all__ = ["ConstrainedGenericType"]

from wich._ident import NameIdent


@dataclass
class ConstrainedGenericType:
    ident: NameIdent
    # [TODO] replace with type once language model done
    bound: NameIdent
