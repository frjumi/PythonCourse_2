class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id}, name=\'{self.name}\', pages={self.pages})'


class Library:
    def __init__(self, books=None):
        self.books = books or []

    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

    def add_book(self, book):
        self.books.append(book)

    def remove_book_by_id(self, book_id):
        index = self.get_index_by_book_id(book_id)
        del self.books[index]


# Пример использования:
if __name__ == '__main__':
    # Инициализация книг
    book_1 = Book(id_=1, name='Тестовая книга 1', pages=200)
    book_2 = Book(id_=2, name='Тестовая книга 2', pages=150)

    # Инициализация пустой библиотеки
    library = Library()

    next_book_id = library.get_next_book_id()
    print(f'Следующий id для новой книги: {next_book_id}')

    # Добавление книг в библиотеку
    library.add_book(book_1)
    library.add_book(book_2)

    # Вывод информации о книгах, содержащихся в библиотеке
    for book in library.books:
        print(book)

    # Получение следующего id для добавления новой книги
    next_book_id = library.get_next_book_id()
    print(f'Следующий id для новой книги: {next_book_id}')

    # Вывод индекса книги по её id
    for book_id_to_find in range(1, 4):
        try:
            book_index = library.get_index_by_book_id(book_id_to_find)
            print(f'Индекс книги с id={book_id_to_find}: {book_index}')
        except ValueError as e:
            print(e)