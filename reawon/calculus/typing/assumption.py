from dataclasses import dataclass


@dataclass
class Assumption:
    variable: str
    type: type
