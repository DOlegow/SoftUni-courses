from problems_1_2.project import Bird
from problems_1_2.project import Meat


class Owl(Bird):
    WEIGHT_INCREASE = 0.25

    def make_sound(self) -> str:
        return "Hoot Hoot"

    def feed(self, food) -> str:
        if isinstance(food, Meat):
            self.weight += food.quantity * self.WEIGHT_INCREASE
            self.food_eaten += food.quantity
        else:
            return f"Owl does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"Owl [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Hen(Bird):
    WEIGHT_INCREASE = 0.35

    def make_sound(self) -> str:
        return "Cluck"

    def feed(self, food) -> str:
        self.weight += food.quantity * self.WEIGHT_INCREASE
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"Hen [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
