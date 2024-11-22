from project.computer_types.computer import Computer


class Laptop(Computer):
    VALID_PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200,
    }
    MAX_RAM = 64

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.VALID_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
        if ram > self.MAX_RAM or ram & (ram - 1) != 0:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = self.VALID_PROCESSORS[processor] + (ram.bit_length() - 1) * 100
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."
