from dataclasses import dataclass

from ..identifier import Identifier
from .body import Body
from .head import Head


__all__ = ["Lambda"]


class Lambda:
    name: Identifier
    head: Head
    body: Body
