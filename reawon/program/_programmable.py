"""

    *Programmable*

  (or just describable)

"""

from abc import ABCMeta

__all__ = ["Programmable"]


class Programmable:
    __metaclass__ = ABCMeta


class LogicalProof(
    Programmable,
    Analysis,
):
    pass


class LogicalEquivalence(
    Programmable,
    Analysis,
):
    pass


class LogicalTruth(
    Programmable,
    Analysis,
):
    pass
