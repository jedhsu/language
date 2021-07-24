from dataclasses import dataclass


from .scope import Scope

@dataclass
class Binding:
    name: str
    scope: Scope
