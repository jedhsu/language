"""

Abstract Transform

An abstract transform is an operator where input and output are unique types.

Interestingly, transforms and morphisms are also a partition of operator! - think about this

Seems like we're getting close to some even more fundamental structuring here... remember this feeling

"""

from typing import TypeVar, Generic

__all__ = ["AbstractTransform"]

from .._operator import AbstractOperator
from ...type import AbstractType

C = TypeVar("C", bound=AbstractType)
D = TypeVar("D", bound=AbstractType)

# [TODO] generic protocols will also seem relevant!

# [TODO] how to specify disjointness?
class AbstractTransform(
    AbstractOperator,
    Generic[C, D],
):
    input: C
    output: D
