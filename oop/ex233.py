"""
Exercise 2.3.3
"""
class Ferret:
    """
    A class representing a ferret
    """
    count_animals: int = 0

    def __init__(self, name: str = "Sam") -> None:
        """
        init function
        :param name: ferrets name
        """
        self._name: str = name
        self._age: int = 0
        Ferret.count_animals += 1

    def birthday(self) -> None:
        """
        increases ferrets age by one
        :return: None
        """
        self._age += 1

    def get_age(self) -> int:
        """
        :return: ferrets age
        """
        return self.age

    def set_name(self, name: str) -> None:
        """
        changes ferrets name
        :param name: the new name
        :return: None
        """
        self._name = name

    def get_name(self) -> str:
        """
        :return: the ferrets name
        """
        return self._name

