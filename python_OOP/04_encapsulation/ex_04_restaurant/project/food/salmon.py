from problems_1_2.project import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name: str, price: float):
        super().__init__(name, price, self.GRAMS)
