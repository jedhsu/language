"""

Type-theoretic models & interfaces.

Start by speccing ideas in PEP 483

"""
from __future__ import annotations
from typing import Any, Callable, Generic, NewType, TypeVar
from typing import Literal, Union

from ..base.expression import Value


class FiniteSet(set):

    pass


class InfiniteSet:
    pass


class Set(set[value]):
    def __leq__(self):
        """
        Subset operation.

        """


T = TypeVar("T")


class _Define_:
    @staticmethod
    def define_from_values(values: set[Value]):
        return Type(values, None)

    @staticmethod
    def define_from_methods(funcs: FiniteSet[Method]):
        """
        This is protocol typing.

        """
        pass

    @staticmethod
    def define_from_classdef(classdef: ClassDefinition):
        """
        This is a syntactically explicit way to define.

        """
        pass

    @staticmethod
    def define_from_operations():
        """
        Define from union and intersection operations.

        """
        pass


Any = Literal["Any"]

TypeOrAny = Union[Type, Any]


class Consistent:
    @staticmethod
    def is_consistent_to(t1: TypeOrAny, t2: TypeOrAny) -> bool:
        if t1 == Any or t2 == Any:
            return True

        return is_subtype_of(t1, t2)


Operation = NewType("Operation", Callable[Value, Any])
Domain = set[Value]  # use the word space for this instead? meh
# Operation = Callable[[Domain], Domain]  # make a custom type for this

# this results in rigorous typedef


class Type(Generic[T], _Define_):
    """
    A type is a domain (a set of values) imbued with a set of operations defined between domains.

    """

    values: Domain  # possibly infinite, extend later
    operations: set[Operation]


"""

Now, our strategy is to consolidate building blocks into a slightly higher level base type with composition operations. 

Intuitively, we have

Dict subtypes Set.
List subtypes Set.



Essentially, since Callable and Tuple are also Types, all Operations are some Mapping from Type to Type

Does there really need to be a further restriction on "Type Constructors" then?

"""

X = Type
Y = Type

"""

Frame this using applicatives, looks like it fits.

"""


class Operator(Generic[X, Y]):
    """
    This is the general operator class...

    """

    input: Type
    output: Type
    function: Callable[X, Y]

    def arity(self):
        if type(input) == tuple:
            return len(self.input)


# [TODO] math is way messed up on this, fix it
class _Type_(Type, tuple[Type], dict[Type]):
    def __add__(self):
        """
        Set union.

        """

    def __sub__(self):
        pass


"""

[Testing]

"""

# # Animal = ...
# Dog = Type(values={"Shepherd", "Poodle", "Pekingnese"})


# class Dog:
