import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class Country:
    def __init__(self, name: str, population: float, area: float, gdp: float):
        """
        Создание и подготовка к работе объекта "Страна"

        :param name: Название страны
        :param population: Население страны
        :param area: Площадь страны
        :param gdp: ВВП страны

        Примеры:
        >>> country = Country("Российская Федерация", 146150789, 17125191, 5180000000000)
        """
        if not isinstance(name, str):
            raise TypeError("Название страны должно быть типа str")
        self.name = name

        if not isinstance(population, (int, float)):
            raise TypeError("Население страны должно быть типа int или float")
        if population < 0:
            raise ValueError("Население страны должно быть положительным числом")
        self.population = population

        if not isinstance(area, (int, float)):
            raise TypeError("Площадь страны должна быть типа int или float")
        if area < 0:
            raise ValueError("Площадь страны должна быть положительным числом")
        self.area = area

        if not isinstance(gdp, (int, float)):
            raise TypeError("ВВП страны должен быть типа int или float")
        if gdp < 0:
            raise ValueError("ВВП страны должен быть положительным числом")
        self.gdp = gdp

    def calculate_population_density(self) -> float:
        """
        Функция, которая рассчитывает плотность населения (население разделить на площадь)

        :return: Плотность населения

        Примеры:
        >>> country = Country("Российская Федерация", 146150789, 17125191, 5180000000000)
        >>> country.calculate_population_density()
        """
        ...

    def calculate_per_capita_gdp(self) -> float:
        """
        Функция, которая рассчитывает ВВП на душу населения (ВВП разделить на население)

        :return: ВВП на душу населения

        Примеры:
        >>> country = Country("Российская Федерация", 146150789, 17125191, 5180000000000)
        >>> country.calculate_per_capita_gdp()
        """
        ...


class Rectangle:
    def __init__(self, length: float, width: float):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param length: Длина прямоугольника
        :param width: Ширина прямоугольника

        Примеры:
        >>> rectangle = Rectangle(100, 50)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина прямоугольника должна быть типа int или float")
        if not length > 0:
            raise ValueError("Длина прямоугольника должна быть больше 0")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина прямоугольника должна быть типа int или float")
        if not width > 0:
            raise ValueError("Ширина прямоугольника должна быть больше 0")
        self.width = width

    def calculate_perimeter(self) -> float:
        """
        Функция, которая рассчитывает периметр прямоугольника

        :return: Периметр прямоугольника

        Примеры:
        >>> rectangle = Rectangle(100, 50)
        >>> rectangle.calculate_perimeter()
        """
        ...

    def calculate_area(self) -> float:
        """
        Функция, которая рассчитывает площадь прямоугольника

        :return: Площадь прямоугольника

        Примеры:
        >>> rectangle = Rectangle(100, 50)
        >>> rectangle.calculate_area()
        """
        ...


class ElectricKettle:
    def __init__(self, power: float, capacity: float, water_volume: float):
        """
        Создание и подготовка к работе объекта "Электрический чайник"

        :param power: Мощность чайника в ваттах (Вт)
        :param capacity: Общая вместимость чайника в литрах
        :param water_volume: Текущий объем воды в чайнике в литрах

        Примеры:
        >>> kettle = ElectricKettle(2000, 1.5, 1)  # инициализация экземпляра класса
        """
        if not isinstance(power, (int, float)) or power <= 0:
            raise ValueError("Мощность должна быть положительным числом типа int или float")
        self.power = power

        if not isinstance(capacity, (int, float)) or capacity <= 0:
            raise ValueError("Вместимость должна быть положительным числом типа int или float")
        self.capacity = capacity

        if not isinstance(water_volume, (int, float)) or water_volume < 0:
            raise ValueError("Объем воды должен быть неотрицательным числом типа int или float")
        if water_volume > capacity:
            raise ValueError("Объем воды не может превышать вместимость чайника")
        self.water_volume = water_volume

    def calculate_energy_consumed(self, hours: float) -> float:
        """
        Рассчитывает количество электроэнергии, потребленной чайником за определенное время.

        :param hours: Время работы чайника в часах

        :return: Потребленная электроэнергия в киловатт-часах (кВт·ч)

        Примеры:
        >>> kettle = ElectricKettle(2000, 1.5, 1)
        >>> kettle.calculate_energy_consumed(2)
        """
        if not isinstance(hours, (int, float)) or hours <= 0:
            raise ValueError("Время работы должно быть положительным числом типа int или float")
        ...

    def calculate_daily_cost(self, rate_per_kwh: float, usage_hours_per_day: float) -> float:
        """
        Определяет стоимость работы чайника за сутки, исходя из стоимости электроэнергии и времени использования.

        :param rate_per_kwh: Тариф оплаты за 1 кВт·ч
        :param usage_hours_per_day: Среднее количество часов использования в день

        :return: Стоимость работы чайника за сутки

        Примеры:
        >>> kettle = ElectricKettle(2000, 1.5, 1)
        >>> kettle.calculate_daily_cost(5, 3)
        """
        if not isinstance(rate_per_kwh, (int, float)) or rate_per_kwh <= 0:
            raise ValueError("Тариф должен быть положительным числом типа int или float")
        if not isinstance(usage_hours_per_day, (int, float)) or usage_hours_per_day <= 0:
            raise ValueError("Часы использования в день должны быть положительным числом типа int или float")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
