"""

    *Environment*

  Environment :: State

  Contains the state of variable values and bindings.

"""

from abc import ABCMeta


class Environment(
    State,
):
    __metaclass__ = ABCMeta
