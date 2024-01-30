class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self.__name

    @property
    def author(self) -> str:
        return self.__author


class PaperBook(Book):
    def __init__(self, name, author, pages: int):
        super().__init__(name=name, author=author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Неверный тип данных")
        if pages <= 0:
            raise ValueError("Количество страниц не может быть равным 0 или отрицательному числу")
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name, author, duration: float):
        super().__init__(name=name, author=author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError("Неверный тип данных")
        if duration <= 0:
            raise ValueError("Продолжительность аудиокниги не может быть равна 0 или отрицательному числу")
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == '__main__':
    # Объект класса Book
    book_1 = Book("Пикник на обочине", "А.Н. Стругацкий, Б.Н.Стругацкий")
    print(book_1)
    print(repr(book_1))

    book_1_in_paper = PaperBook(book_1.name, book_1.author, 256)
    print(book_1_in_paper)
    print(repr(book_1_in_paper))

    # Объект класса PaperBook
    paper_1 = PaperBook("Ведьмак. Меч Предназначения", "Анджей Сапковский", 384)
    print(paper_1)
    print(repr(paper_1))

    # Объект класса AudioBook
    audio_1 = AudioBook("Кэрри", "Стивен Кинг", 7.39)
    print(audio_1)
    print(repr(audio_1))

    # Изменение кол-ва страниц в paper_1
    paper_1.pages = 431
    print(paper_1)
    print(repr(paper_1))

    #Изменение продолжительности audio_1
    audio_1.duration = 4.1
    print(audio_1)
    print(repr(audio_1))