from datetime import datetime

if __name__ == "__main__":
    # Write your solution here
    class Car:
        """Базовый класс для автомобилей."""

        def __init__(self, brand: str, model: str, year: int, engine_power: int):
            """
            Инициализация автомобиля.

            :param brand: Марка автомобиля.
            :param model: Модель автомобиля.
            :param year: Год выпуска.
            :param engine_power: Мощность двигателя, л.с.
            """
            self.brand = brand
            self.model = model
            self.year = year
            self.engine_power = engine_power

        @property
        def engine_power(self) -> int:
            return self._engine_power

        @engine_power.setter
        def engine_power(self, value: int):
            if not (50 <= value <= 1000):
                raise ValueError("Мощность двигателя должна быть от 50 до 1000 л.с.")
            self._engine_power = value

        @property
        def year(self) -> int:
            return self._year

        @year.setter
        def year(self, value: int):
            if not (value <= datetime.now().year + 1):
                raise ValueError("Год выпуска не может быть больше текущего года.")
            self._year = value

        def get_age(self) -> int:
            """Вычислить возраст автомобиля."""
            return datetime.now().year - self.year

        def pay_tax(self) -> str:
            """Оплата транспортного налога."""
            return "Метод расчета налога не задан."

        def __str__(self) -> str:
            return f"{self.brand} {self.model} ({self.year}), {self.engine_power} л.с."

        def __repr__(self) -> str:
            return (f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, "
                    f"year={self.year!r}, engine_power={self.engine_power!r})")


    class PassengerCar(Car):
        """Легковой автомобиль."""

        def __init__(self, brand: str, model: str, year: int, engine_power: int, passengers: int):
            """
            Инициализация легкового автомобиля.

            :param brand: Марка автомобиля.
            :param model: Модель автомобиля.
            :param year: Год выпуска.
            :param engine_power: Мощность двигателя, л.с.
            :param passengers: Количество пассажиров.
            """
            super().__init__(brand, model, year, engine_power)
            self.passengers = passengers

        @property
        def passengers(self) -> int:
            return self._passengers

        @passengers.setter
        def passengers(self, value: int):
            if value < 1:
                raise ValueError("Легковой автомобиль должен вмещать хотя бы одного пассажира.")
            self._passengers = value

        def pay_tax(self) -> str:
            """
            Оплата транспортного налога.

            Например, будем считать, что для легковых автомобилей налог рассчитывается по формуле:
            налог = мощность двигателя (л.с.) × 12 рублей.
            """
            tax_amount = self.engine_power * 12
            return f"Транспортный налог для {self.brand} {self.model}: {tax_amount} рублей."

        def __str__(self) -> str:
            return f"{super().__str__()}, {self.passengers} пассажиров"

        def __repr__(self) -> str:
            return (f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, "
                    f"year={self.year!r}, engine_power={self.engine_power!r}, passengers={self.passengers!r})")


    class Truck(Car):
        """Грузовой автомобиль."""

        def __init__(self, brand: str, model: str, year: int, engine_power: int, cargo_capacity: float):
            """
            Инициализация грузового автомобиля.

            :param brand: Марка автомобиля.
            :param model: Модель автомобиля.
            :param year: Год выпуска.
            :param engine_power: Мощность двигателя, л.с.
            :param cargo_capacity: Грузоподъёмность (в тоннах).
            """
            super().__init__(brand, model, year, engine_power)
            self.cargo_capacity = cargo_capacity

        def pay_tax(self) -> str:
            """
            Оплата транспортного налога.

            Например, будем считать, что для грузовых автомобилей налог рассчитывается по формуле:
            налог = мощность двигателя (л.с.) × 20 рублей.
            """
            tax_amount = self.engine_power * 20
            return f"Транспортный налог для {self.brand} {self.model}: {tax_amount} рублей."

        def __str__(self) -> str:
            return f"{super().__str__()}, грузоподъёмность: {self.cargo_capacity} т"

        def __repr__(self) -> str:
            return (f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, "
                    f"year={self.year!r}, engine_power={self.engine_power!r}, cargo_capacity={self.cargo_capacity!r})")

    car = PassengerCar("Toyota", "Camry", 2022, 150, 5)
    print(car.__repr__())    # PassengerCar(brand='Toyota', model='Camry', year=2022, engine_power=150, passengers=5)
    print(car.__str__())     # Toyota Camry (2022), 150 л.с., 5 пассажиров
    print(car.pay_tax())     # Транспортный налог для Toyota Camry: 1800 рублей.
    print(car.get_age())     # 3

    truck = Truck("Volvo", "FH16", 2020, 400, 30)
    print(truck.__repr__())  # Truck(brand='Volvo', model='FH16', year=2020, engine_power=400, cargo_capacity=30)
    print(truck.__str__())   # Volvo FH16 (2020), 400 л.с., грузоподъёмность: 30 т
    print(truck.pay_tax())   # Транспортный налог для Volvo FH16: 8000 рублей.
    print(truck.get_age())   # 5

    pass
