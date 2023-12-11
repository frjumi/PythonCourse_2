import doctest


class Sportsman:
    def __init__(self, name: str, awards: int, number_of_workouts: int):
        """
        Создание и подготовка к работе объекта "Спортсмен"

        :param name: Имя спортсмена
        :param awards: Количество наград
        :param number_of_workouts: Количество тренировок в неделю

        Примеры:
        >>> sportsman = Sportsman("Леонид", 10, 3)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя спортсмена должно быть типа str")
        self.name = name

        if not isinstance(awards, int):
            raise TypeError("Количество наград должно быть типа int")
        self.awards = awards

        if not isinstance(number_of_workouts, int):
            raise TypeError("Количество тренировок должно быть типа int")
        self.number_of_workouts = number_of_workouts

    def increase_the_number_of_workouts(self, number: int) -> None:
        """
        Функция, которая позволяет повысить количество тренировок у спортсмена.

        :param number: На сколько повысить количество тренировок.

        Примеры:
        >>> sportsman = Sportsman("Леонид", 10, 3)
        >>> sportsman.increase_the_number_of_workouts(2)
        """
        ...

    def running_around_the_stadium(self, number_of_circles) -> None:
        """
        Функция, которая заставляет спортсмена бежать вокруг стадиона заданное количество кругов.

        :param number_of_circles: Сколько кругов спортсмен должен пробежать вокруг стадиона.

        Примеры:
        >>> sportsman = Sportsman("Леонид", 10, 3)
        >>> sportsman.running_around_the_stadium(2)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
