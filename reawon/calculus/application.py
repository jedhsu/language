from dataclasses import dataclass

from ..term import Term


@dataclass
class Application(Term):
    left: Term
    right: Term
