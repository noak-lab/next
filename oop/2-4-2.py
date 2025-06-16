class BigThing:
    def __init__(self, thing) -> None:
        self._thing = thing

    def size(self) -> int:
        if type(self._thing) == int:
            return int
        return len(self._thing)


class BigCat(BigThing):
    """
    A class representing a cat
    """
    def __init__(self, thing, weight) -> None:
        """
        init function
        :param thing: cats name
        :param weight: cats weight
        """
        BigThing.__init__(self, thing)
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
