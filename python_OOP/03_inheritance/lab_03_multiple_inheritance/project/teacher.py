from problems_1_2.project import Employee
from problems_1_2.project import Person


class Teacher(Employee, Person):
    def teach(self):
        return "teaching..."
