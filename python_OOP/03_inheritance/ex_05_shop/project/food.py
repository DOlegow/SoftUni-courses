from problems_1_2.project import Product


class Food(Product):
    def __init__(self, name):
        super().__init__(name, 15)