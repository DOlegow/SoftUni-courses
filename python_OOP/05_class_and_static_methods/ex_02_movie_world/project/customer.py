from problems_1_2.project import DVD


class Customer:
    def __init__(self, name: str, age: int, uid: int):
        self.name = name
        self.age = age
        self.id = uid
        self.rented_dvds: list[DVD] = []

    def __repr__(self):
        return (f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} "
                f"rented DVD's ({', '.join([dvd.name for dvd in self.rented_dvds])})")

