from typing import GenericAlias, Literal, Union

from ...choice import Choice
from ..symbol.symbol import Symbol


EmptyString = Literal["ε"]

# figure out this type class issue
class OneOf:
    __class_getitem__ = classmethod(GenericAlias)


class _Atom_(Symbol):
    ...
