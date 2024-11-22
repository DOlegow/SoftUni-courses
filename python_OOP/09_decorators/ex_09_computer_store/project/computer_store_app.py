from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)
        elif type_computer == "Laptop":
            computer = Laptop(manufacturer, model)
        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        configuration_message = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return configuration_message

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if (
                computer.price <= client_budget
                and computer.processor == wanted_processor
                and computer.ram >= wanted_ram
            ):
                self.warehouse.remove(computer)
                self.profits += client_budget - computer.price
                return f"{computer} sold for {client_budget}$."
        raise Exception("Sorry, we don't have a computer for you.")
