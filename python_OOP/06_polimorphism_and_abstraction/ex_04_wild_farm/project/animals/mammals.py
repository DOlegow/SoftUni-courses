from problems_1_2.project import Mammal
from problems_1_2.project import Vegetable, Fruit, Meat


class Mouse(Mammal):
    WEIGHT_INCREASE = 0.10

    def make_sound(self) -> str:
        return "Squeak"

    def feed(self, food) -> str:
        if isinstance(food, (Vegetable, Fruit)):
            self.weight += food.quantity * self.WEIGHT_INCREASE
            self.food_eaten += food.quantity
        else:
            return f"Mouse does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"Mouse [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Dog(Mammal):
    WEIGHT_INCREASE = 0.40

    def make_sound(self) -> str:
        return "Woof!"

    def feed(self, food) -> str:
        if isinstance(food, Meat):
            self.weight += food.quantity * self.WEIGHT_INCREASE
            self.food_eaten += food.quantity
        else:
            return f"Dog does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"Dog [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Cat(Mammal):
    WEIGHT_INCREASE = 0.30

    def make_sound(self) -> str:
        return "Meow"

    def feed(self, food) -> str:
        if isinstance(food, (Vegetable, Meat)):
            self.weight += food.quantity * self.WEIGHT_INCREASE
            self.food_eaten += food.quantity
        else:
            return f"Cat does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"Cat [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Tiger(Mammal):
    WEIGHT_INCREASE = 1.00

    def make_sound(self) -> str:
        return "ROAR!!!"

    def feed(self, food) -> str:
        if isinstance(food, Meat):
            self.weight += food.quantity * self.WEIGHT_INCREASE
            self.food_eaten += food.quantity
        else:
            return f"Tiger does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"Tiger [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
