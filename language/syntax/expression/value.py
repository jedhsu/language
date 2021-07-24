"""

Value is a fully evaluated expression.

More precisely, Value is a Code Graph with length = 1.

Note that code graphs could have infinite length.

Simplest example is the infinite loop.

"""

# this will be an interesting type

from .base import Expression


class Value(Expression, Graph):
    # Every value has a type.
    type: type
