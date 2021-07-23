from .base import TypeSystem
from .unbounded import Unbounded

__all__ = ["Relevant"]


class Relevant(
    Unbounded,
    TypeSystem,
):
    pass
