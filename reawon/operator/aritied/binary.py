from abc import ABCMeta
from dataclasses import dataclass

__all__ = ["AbstractBinaryOperator"]

"""

An abstract operator of arity 2.

"""

from language.constant import Constant

from .base import AbstractAritiedOperator


@dataclass
class AbstractBinaryOperator(
    AbstractAritiedOperator,
):
    __metaclass__ = ABCMeta

    left: AbstractExpression
    right: AbstractExpression

    @classmethod
    def from_ast(cls: type[T], node: ast.BinOp) -> T:
        return cls(
            OperatorSymbol.from_ast(node.op),
            Constant.from_ast(node.left),
            Constant.from_ast(node.right),
        )

    def into_ast(self) -> ast.BinOp:
        return self._node(
            self.left.into_ast(),
            self.operator.into_ast(),
            self.right.into_ast(),
        )
