from abc import ABC


class FormulaTeam(ABC):
    MONEY_NEEDED = 1_000_000

    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget
    
    @budget.setter
    def budget(self, value):
        if value < self.MONEY_NEEDED:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        raise NotImplementedError("Subclasses must implement this method")
