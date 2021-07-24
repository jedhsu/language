"""

Symbol mapping (table).

"""

from dataclasses import dataclass
from typing import Mapping


@dataclass
class Symbol:
    lexeme: Lexeme
    type: Type
    position: Position


class SymbolMapping(Mapping[_Symbol, Symbol]):
    pass
