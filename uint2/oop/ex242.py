"""
Exercise 2.4.2
"""
class BigThing:
    def __init__(self, thing: any) -> None:
        """
        init function
        :param thing: thing, can be any type
        :return: None
        """
        self._thing: any = thing

    def size(self) -> int:
        """
        returns size according to things type
        :return: size
        """
        if type(self._thing) == int:
            return self._thing
        return len(self._thing)


class BigCat(BigThing):
    """
    A class representing a cat
    """
    def __init__(self, name: any, weight: int) -> None:
        """
        init function
        :param name: cats name
        :param weight: cats weight
        :return: None
        """
        BigThing.__init__(self, name)
        self._weight: int = weight

    def size(self) -> str:
        """
        :return: a string representing the cats size
        """
        if self._weight < 15:
            return "OK"
        if self._weight < 20:
            return "Fat"
        return "Very Fat"
