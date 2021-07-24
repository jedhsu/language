"""

    *Theory*

  Only theory can "structurally develop" a thing.

  Purposely avoidign rigorous definition of type, it has intuitionistic downsides.

"""

from abc import ABCMeta

from ._thing import Thing

__all__ = ["Theory"]


class Theory(
    Thing,
):
    __metaclass__ = ABCMeta
