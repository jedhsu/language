from dataclasses import dataclass


@dataclass
class EvaluationRule(Satisfy):
    left: MetaExpression
    right: MetaExpression
