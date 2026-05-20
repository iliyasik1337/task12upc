class Organism:
    """Базовый класс, представляющий живое существо."""

    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy
        self.is_alive = True

    def eat(self, amount: int):
        """Увеличивает энергию организма."""
        if self.is_alive:
            self.energy += amount
            print(f"{self.name} поел и теперь имеет {self.energy} энергии.")

    def spend_energy(self, amount: int):
        """Тратит энергию и проверяет состояние жизни."""
        self.energy -= amount
        if self.energy <= 0:
            self.is_alive = False
            self.energy = 0


class Animal(Organism):
    """Класс животного, который может активно искать пищу."""

    def move(self):
        """Тратит энергию на движение."""
        if self.is_alive:
            print(f"{self.name} перемещается по локации...")
            self.spend_energy(5)