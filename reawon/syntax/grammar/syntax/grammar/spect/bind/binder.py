from typing import Literal

from .binding import Binding
from .identifier import Identifier

__all__ = ["Binder"]

# -- Effects
EnvBind = Literal[None]


class BindCheck:
    @staticmethod
    def pute_binding(ident: Identifier) -> Binding:
        ...

    @staticmethod
    def bind_bindings(ident: Identifier) -> EnvBind:
        ...


class Binder(BindCheck):
    ...
