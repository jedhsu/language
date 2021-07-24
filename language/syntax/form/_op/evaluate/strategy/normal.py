"""

Normal order.

"""

from .base import EvaluationStrategy


class NormalOrder(EvaluationStrategy):
    def outermost_redex(self):
        pass

    def __next__(self) -> Form:
        """
        Returns the form to be evaluated.

        """
