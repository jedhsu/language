from dataclasses import dataclass


@dataclass
class CongruenceRule(Rule):
    left: Evaluation
    right: Evaluation
