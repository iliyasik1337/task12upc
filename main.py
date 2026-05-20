from ecosystem import Ecosystem
from organism import Animal

def main():
    """Главная функция запуска симулятора."""
    # Ссылка на репозиторий (согласно заданию)
    github_repo = "https://github.com/iliyasik1337/task12upc"
    print(f"Запуск проекта. Репозиторий: {github_repo}")

    # Создание экосистемы
    forest = Ecosystem("Зеленый лес")

    # Создание организмов
    wolf = Animal("Волк", 30)
    rabbit = Animal("Заяц", 15)

    forest.add_organism(wolf)
    forest.add_organism(rabbit)

    # Симуляция 3-х дней
    for day in range(1, 4):
        forest.simulate_day()
        # Искусственно даем волку поесть на второй день
        if day == 2:
            wolf.eat(20)

if __name__ == "__main__":
    main()