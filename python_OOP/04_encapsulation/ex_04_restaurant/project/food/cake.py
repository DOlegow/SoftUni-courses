from problems_1_2.project import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name: str):
        super().__init__(name, self.PRICE, self.GRAMS, self.CALORIES)
