class Pixel:
    """
    A class representing a pixel
    """
    def __init__(self, x: int = 0, y: int = 0, red: int = 0, green: int = 0, blue: int = 0) -> None:
        """
        init functions
        :param x: x coordinate
        :param y: y coordinate
        :param red: a value between 0 and 255
        :param green: a value between 0 and 255
        :param blue: a value between 0 and 255
        """
        self._x: int = x
        self._y: int = y
        self._red: int = red
        self._green: int = green
        self._blue: int = blue

    def set_coords(self, x, y) -> None:
        """
        sets pixel's new coordinate
        :param x: new x coordinate
        :param y: new y coordinate
        :return: None
        """
        self._x = x
        self._y = y

    def set_grayscale(self) -> None:
        """
        Changes pixel's color to grayscale
        :return: None
        """
        avg: int = round((self._red + self._green + self._blue) / 3)
        self._red = avg
        self._blue = avg
        self._green = avg

    def print_pixel_info(self) -> None:
        """
        prints pixel's values
        :return: None
        """
        string: str = f"X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue})"
        if [self._blue, self._red, self._green].count(0) == 2:
            if self._blue > 0:
                string += " Blue\n"
            elif self._red > 0:
                string += " Red\n"
            else:
                string += " Green\n"
        print(string)
