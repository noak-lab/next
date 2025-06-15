class Ferret:
    """
    A class representing a ferret
    """
    count_animals = 0

    def __init__(self, name="Sam"):
        """
        init function
        :param name: ferrets name
        """
        self._name = name
        self._age = 0
        Ferret.count_animals += 1

    def birthday(self):
        """
        increases ferrets age by one
        :return: None
        """
        self._age += 1

    def get_age(self):
        """
        :return: ferrets age
        """
        return self.age

    def set_name(self, name):
        """
        changes ferrets name
        :param name: the new name
        :return: None
        """
        self._name = name

    def get_name(self):
        """
        :return: the ferrets name
        """
        return self._name


class Pixel:
    """
    A class representing a pixel
    """
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        """
        init functions
        :param x: x coordinate
        :param y: y coordinate
        :param red: a value between 0 and 255
        :param green: a value between 0 and 255
        :param blue: a value between 0 and 255
        """
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        """
        sets pixel's new coordinate
        :param x: new x coordinate
        :param y: new y coordinate
        :return: None
        """
        self._x = x
        self._y = y

    def set_grayscale(self):
        """
        Changes pixel's color to grayscale
        :return: None
        """
        avg = round((self._red + self._green + self._blue) / 3)
        self._red = avg
        self._blue = avg
        self._green = avg

    def print_pixel_info(self):
        """
        prints pixel's values
        :return: None
        """
        string = f"X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue})"
        if [self._blue, self._red, self._green].count(0) == 2:
            if self._blue > 0:
                string += " Blue\n"
            elif self._red > 0:
                string += " Red\n"
            else:
                string += " Green\n"
        print(string)


class BigThing:
    def __init__(self, thing):
        self._thing = thing

    def size(self):
        if type(self._thing) == int:
            return int
        return len(self._thing)


class BigCat(BigThing):
    """
    A class representing a cat
    """
    def __init__(self, thing, weight):
        """
        init function
        :param thing: cats name
        :param weight: cats weight
        """
        BigThing.__init__(self, thing)
        self._weight = weight

    def size(self):
        """
        :return: a string representing the cats size
        """
        if self._weight < 15:
            return "OK"
        if self._weight < 20:
            return "Fat"
        return "Very Fat"