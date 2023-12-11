import doctest
from typing import Union


class Cat:
    def __init__(self, name: str, age: Union[int, float], color: str):
        """
        Создание и подготовка к работе объекта "Кот"

        :param name: Имя кота
        :param age: Возраст кота
        :param color: Цвет шерсти кота

        Примеры:
        >>> my_cat = Cat("Васька", 3, "Рыжий")  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя кота должно быть типа str")
        self.name = name

        if not isinstance(age, (int, float)):
            raise TypeError("Возраст кота должен быть типа int или float")
        if age < 0:
            raise ValueError("Возраст кота должен быть положительным числом")
        self.age = age

        if not isinstance(color, str):
            raise TypeError("Цвет шерсти кота должен быть типа str")
        self.color = color

    def feed_the_cat(self) -> None:
        """
        Кормим кота.

        :return: Вывод строки, содержащей следующее предложение "Кот поел, теперь он сытый и довольный."

        Примеры:
        >>> my_cat = Cat("Васька", 3, "Рыжий")
        >>> my_cat.feed_the_cat()
        """
        ...

    @staticmethod
    def give_the_toy(toy: str) -> None:
        """
        Кормим кота.

        :param toy: Игрушка, которую вы хотите дать коту.
        :raise TypeError: Если кот не голоден, он не будет есть.
        :return: Вывод строки, содержащей следующее предложение f"Вы дали коту: {toy}"

        Примеры:
        >>> my_cat = Cat("Васька", 3, "Рыжий")
        >>> my_cat.give_the_toy("Клубок")
        """
        if not isinstance(toy, str):
            raise TypeError("Игрушка должна быть типа str")
        ...


if __name__ == "__main__":
    doctest.testmod()
