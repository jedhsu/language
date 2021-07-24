from abc import ABCMeta, abstractmethod
from typing import Iterator


class EvaluationStrategy(Iterator, metaclass=ABCMeta):
    """
    Defines a total order on evaluation.

    """

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        """
        Returns the next form to be evaluated.

        """
        pass
