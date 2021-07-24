"""

    *Abstract Collection*

  The ideal of an arbitrary (uncountable) collection.

"""

from typing import Any

__all__ = ["AbstractCollection"]


class AbstractCollection:
    # specifies the contained type of this collection
    type: Any

    @classmethod
    def __class_getitem__(cls, item):
        pass
        # [TODO} finish this
