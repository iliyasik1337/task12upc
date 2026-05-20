from organism import Organism

class Ecosystem:
    """Класс, управляющий средой и всеми организмами."""

    def __init__(self, title: str):
        self.title = title
        self.organisms = []

    def add_organism(self, organism: Organism):
        """Добавляет существо в систему."""
        self.organisms.append(organism)
        print(f"{organism.name} добавлен в экосистему {self.title}.")

    def simulate_day(self):
        """Запускает один цикл жизни для всех существ."""
        print(f"\n--- Новый день в экосистеме {self.title} ---")
        for org in self.organisms:
            if org.is_alive:
                # Каждый день тратится базовая энергия на жизнь
                org.spend_energy(10)
                if org.is_alive:
                    print(f"{org.name} активен. Энергия: {org.energy}")
                else:
                    print(f"!!! {org.name} погиб от истощения.")
            else:
                print(f"{org.name} всё еще мертв.")