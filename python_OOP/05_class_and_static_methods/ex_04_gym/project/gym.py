from problems_1_2.project import Customer
from problems_1_2.project import Equipment
from problems_1_2.project import ExercisePlan
from problems_1_2.project import Subscription
from problems_1_2.project import Trainer

class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = next(s for s in self.subscriptions if s.id == subscription_id)
        customer = next(c for c in self.customers if c.id == subscription.customer_id)
        trainer = next(t for t in self.trainers if t.id == subscription.trainer_id)
        equipment = next(e for e in self.equipment if e.id == self.plans[subscription.exercise_id - 1].equipment_id)
        plan = next(p for p in self.plans if p.id == subscription.exercise_id)

        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"
