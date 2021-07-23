from abc import ABC


class Derive:
    # TODO: this should arguably just be from
    @staticmethod
    def derive_from(rule: Rule) -> String:
        ...


class String(Derive, ABC):
    ...
