"""

Introduce a syntax on type bounds and composition.

I favor this because I think it's good to promote that the type tree forms an ordering.

"""


from typing import Type as _Type
from typing import Generic

from ..operation import Operation

# [TODO] figure out the metaclass hacking later, spec the logic first with an encapsulated type

class Equivalence:
    _type: type

    def __eq__(self, t: type):
        return self._type == t


# define a relation on types

# can make relation itself generic later
# need BinaryComparisonOperation

class TypeRelation(Generic[type], Operation.Binary):
    def __call__(self):
        pass

# [TODO] glue above and bottom

def subtype_of(


class Type(PartialOrder, Equivalence):
    _type: type



