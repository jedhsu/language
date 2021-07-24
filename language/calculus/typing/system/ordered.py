from .base import TypeSystem
from .linear import Linear

__all__ = ["Ordered"]


class Ordered(Linear, TypeSystem):
    pass
