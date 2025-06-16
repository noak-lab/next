class Animal:
    """
    A class representing an animal
    """
    zoo_name: str = "Hayaton"

    def __init__(self, name: str, hunger: int = 0) -> None:
        """
        init function
        :param name: animals name
        :param hunger: animals hunger level
        """
        self._name: str = name
        self._hunger: int = hunger

    def get_name(self) -> str:
        """
        :return: animals name
        """
        return self._name

    def is_hungry(self) -> bool:
        """
        :return: true if animal is hungry, false otherwise
        """
        return self._hunger > 0

    def feed(self) -> None:
        """
        feeds animal - lowers hunger level
        :return: None
        """
        if self._hunger > 0:
            self._hunger -= 1

    def talk(self) -> None:
        """
        prints animals phrase - needs to be defined in inheriting classes
        :return: None
        """
        pass


class Dog(Animal):
    """
    A class representing a dog
    """
    def talk(self) -> None:
        """
        prints dogs phrase
        :return: None
        """
        print("woof woof")

    def fetch_stick(self) -> None:
        """
        fetches stick
        :return: None
        """
        print("There you go, sir!")


class Cat(Animal):
    """
    A class representing a cat
    """
    def talk(self) -> None:
        """
        prints cats phrase
        :return: None
        """
        print("meow")

    def chase_laser(self) -> None:
        """"
        chases laser
        :return: None
        """
        print("Meeeeow")


class Skunk(Animal):
    """
    A class representing a skunk
    """
    def __init__(self, name: str, hunger: int, stink_count: int = 6) -> None:
        """
        init function
        :param name: skunks name
        :param hunger: skunks hunger level
        :param stink_count: skunks stick count
        """
        Animal.__init__(self, name, hunger)
        self._stink_count: int = stink_count

    def talk(self) -> None:
        """
        prints skunks phrase
        :return: None
        """
        print("tsssss")

    def stink(self) -> None:
        """
        stinks
        :return: None
        """
        print("Dear lord!")


class Unicorn(Animal):
    """
    A class representing a unicorn
    """
    def talk(self) -> None:
        """
        prints unicorn phrase
        :return: None
        """
        print("Good day, darling")

    def sing(self) -> None:
        """
        makes unicorn sing
        :return: None
        """
        print("I’m not your toy...	")


class Dragon(Animal):
    """
    A class representing a dragon
    """
    def __init__(self, name: str, hunger: int, color: str = "Green") -> None:
        """
        init function
        :param name: dragons name
        :param hunger: dragons hunger level
        :param color: dragons color
        """
        Animal.__init__(self, name, hunger)
        self._color: str = color

    def talk(self) -> None:
        """
        prints dragons phrase
        :return: None
        """
        print("Raaaawr")

    def breath_fire(self) -> None:
        """
        makes dragon breath fire
        :return: None
        """
        print("$@#$#@$	")