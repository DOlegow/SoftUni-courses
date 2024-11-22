class Computer:
    def __init__(self, manufacturer: str, model: str):
        if not manufacturer.strip():
            raise ValueError("Manufacturer name cannot be empty.")
        if not model.strip():
            raise ValueError("Model name cannot be empty.")
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    def configure_computer(self, processor: str, ram: int):
        raise NotImplementedError("This method should be implemented by subclasses.")

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
