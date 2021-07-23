from abc import ABCMeta

from sympy import Lambda
from sympy.sets.fancysets import ImageSet

__all__ = ["Term"]


# can anything meaningful be accomplished by going Token(Syntax)


class Generate:
    def Set(self, index: int) -> ImageSet:
        """
        Generate the syntax terms of a language for the next layer.

        """

        # [TODO] needs more thought
        # return ImageSet(index)
        pass

    class Conditions:
        def closure_under_abstract_rule(self):
            pass


class Term(metaclass=ABCMeta):
    def is_normal(self, evaluation_rules) -> bool:
        """
        Checks if the term is in normal form.

        This implies term is value.
        """

        raise NotImplementedError
