from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    VALID_PROCESSORS = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800,
    }
    MAX_RAM = 128

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.VALID_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
        if ram > self.MAX_RAM or ram & (ram - 1) != 0:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = self.VALID_PROCESSORS[processor] + (ram.bit_length() - 1) * 100
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."
