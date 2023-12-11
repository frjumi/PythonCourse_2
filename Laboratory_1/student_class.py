import doctest


class Student:
    def __init__(self, name: str, surname: str, average_mark: float, course: int):
        """
        Создание и подготовка к работе объекта "Студент"

        :param name: Имя студента
        :param surname: Фамилия студента
        :param average_mark: Средний балл
        :param course: int

        Примеры:
        >>> student_1 = Student("Леонид", "Каневский", 5.0, 3)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя студента должно быть типа str")
        self.name = name

        if not isinstance(surname, str):
            raise TypeError("Фамилия студента должно быть типа str")
        self.surname = surname

        if not isinstance(average_mark, float):
            raise TypeError("Средний балл студента должен быть типа float")
        if average_mark < 2.0:
            raise ValueError("Средний балл студента не должен быть меньше 2.0")
        self.average_mark = average_mark

        if not isinstance(course, int):
            raise TypeError("Номер курса студента должен быть типа int")
        self.course = course

    def is_there_a_scholarship(self) -> bool:
        """
        Функция, которая позволяет узнать, есть у студента стипендия.

        :return: Есть ли стипендия.

        Примеры:
        >>> student_1 = Student("Леонид", "Каневский", 5.0, 3)
        >>> student_1.is_there_a_scholarship()
        """
        ...

    def increase_the_course_number(self, number: int) -> None:
        """
        Функция, которая позволяет повысить номер курса у студента.

        :param number: На сколько повысить номер курса.

        Примеры:
        >>> student_1 = Student("Леонид", "Каневский", 5.0, 3)
        >>> student_1.increase_the_course_number(2)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
