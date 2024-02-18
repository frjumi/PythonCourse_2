from typing import Union, List


class Steam:
    """
        Базовый класс для аккаунта Steam.
    """

    def __init__(self, username: str, login: str, password: Union[str, int]):
        """
                Инициализация объекта Steam.
                :param username: Имя (ник) Steam аккаунта.
                :param login: Логин аккаунта. Непубличный, чтобы пользователь не смог случайно его изменить.
                :param password: Пароль аккаунта. Непубличный, чтобы пользователь не смог случайно его изменить.
        """
        self.username = username
        self.__login = login
        self.__password = password

    @property
    def login(self):
        """Геттер не принимает никаких агрументов, но должен возвращать содержимое login."""
        return self.__login

    def login_change(self, login: str) -> None:
        """
            Меняет логин пользователя
        """
        if not isinstance(login, str):
            raise TypeError("Invalid data type")
        self.__login = login

    @property
    def password(self):
        """Геттер не принимает никаких агрументов, но должен возвращать содержимое password."""
        return self.__password

    def change_password(self, password: Union[str, int]) -> None:
        """
            Меняет пароль пользователя
        """
        if not isinstance(password, Union[str, int]):
            raise TypeError("Invalid data type")
        if not 8 <= password <= 29:
            raise AssertionError("The password must not contain less than 8 and more than 29 characters")
        self.__password = password

    def __str__(self) -> str:
        """
        Возвращает строку с информацией о Steam.

        Возвращает:
        - str: строка с информацией о Steam
        """
        return (f"Steam: Your username = {self.username}. "
                f"Other attributes can be seen by special call.")

    def __repr__(self) -> str:
        """
        Возвращает строку, содержащую полное название класса и значение атрибутов класса.

        Возвращает:
        - str: строка, содержащая полное название класса и значение атрибутов username, login, password
        """
        return (f"{self.__class__.__name__}(username={self.username!r}, login={self.login!r}, "
                f"password={self.password!r})")

    def login_to_account(self) -> None:
        """
            Выполняет вход в аккаунт. В данном случае в Steam аккаунт.
        """
        pass


class GameLibrary(Steam):
    """
        Дочерний класс GameLibrary.
    """

    def __init__(self, username, login, password, number_of_games: int, games: List[str]):
        """
        Инициализирует объект класса GameLibrary.

        Аргументы:
        :param username (str): имя аккаунта, обладающего данной библиотекой GameLibrary
        :param login: логин аккаунта
        :param password: пароль аккаунта
        :param number_of_games: количество игр на аккаунте
        :param games (List[str]): список игр GameLibrary
        """
        super().__init__(username=username, login=login, password=password)
        self.number_of_games = number_of_games or 0
        self.games = games

    def __str__(self) -> str:
        """
        Возвращает строку с информацией о GameLibrary.

        Возвращает:
        - str: строка с информацией о GameLibrary
        """
        return (f"GameLibrary: Your username = {self.username}. Number of games on account = {self.number_of_games}. "
                f"List of available games = {self.games}.")

    def __repr__(self) -> str:
        """
        Возвращает строку, содержащую полное название класса и значение атрибутов класса.

        Возвращает:
        - str: строка, содержащая полное название класса и значение атрибутов username, login, password
        """
        return (f"{self.__class__.__name__}(username={self.username!r}, login={self.login!r}, "
                f"password={self.password!r}, number_of_games={self.number_of_games!r}, "
                f"games={self.games!r})")

    def show_games(self) -> None:
        """
        Выводит список игр GameLibrary.
        """
        print(f"Игры в GameLibrary '{self.username}':")
        for game in self.games:
            print(game)

    def play_game(self, game: str) -> None:
        """
        Играет в указанную игру из GameLibrary.

        Аргументы:
        - game (str): игра для игры
        """
        if game in self.games:
            print(f"Играем в игру '{game}' из GameLibrary")
        else:
            raise AssertionError("This game is not in your library")

    def login_to_account(self) -> None:
        """
            Выполняет вход в аккаунт. В данном случае в аккаунт определённой игры.

            Перегрузка необходима т.к. в некоторых играх может устанавливаться свой логин и пароль,
            который в последствии нужно ввести.
        """
        pass


if __name__ == "__main__":
    acc = Steam("cat", "meow", 12344567)
    print(acc)
    print(repr(acc))
    library = GameLibrary(acc.username, acc.login, acc.password, 2,
                          ["Stardew Valley", "The Witcher 3"])
    print(library)
    print(repr(library))
    library.show_games()
    library.play_game("Stardew Valley")
    # library.play_game("Raft")
