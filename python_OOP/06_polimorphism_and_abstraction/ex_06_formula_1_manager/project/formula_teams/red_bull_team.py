from problems_1_2.project import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        if race_pos == 1:
            revenue += 1_500_000  # Oracle sponsorship
        elif race_pos == 2:
            revenue += 800_000
        if race_pos <= 8:
            revenue += 20_000     # Honda sponsorship
        elif race_pos <= 10:
            revenue += 10_000
        revenue -= 250_000  # Red Bull expenses per race
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
