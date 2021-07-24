"""

    *Subtyping*

  The subtype relation.

"""

from .type import AbstractType


class Subtyping(AbstractType):
    """
    Subtyping.
    """

    def is_values_superset_of(self, t: AbstractType):
        """
        Is the values set of t1 a superset of the values set of t2?
        i.e. is an arbitrary value of t2 contained in t1?

        This is obviously not determinable without a different mechanism.
        """
        raise NotImplementedError

    def is_operators_subset_of(self, t: AbstractType):
        """
        Is an arbitrary operation of t1 contained in t2?
        """
        return self.operators in t.operators

    def is_subtype_of(
        self,
        t: AbstractType,
        is_values_superset: bool,
    ) -> bool:
        """

        Subtype criterion:
        * Every value of t1 is in the values of t2
        * Every operation of t1 is in the operations of t2

        Use subset operator.

        """
        return is_values_superset and self.is_operators_subset_of(t)
