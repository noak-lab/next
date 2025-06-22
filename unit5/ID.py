from __future__ import annotations
from typing import Generator, Iterator
MAX_ID: int = 999999999


def check_id_valid(id_number: int) -> bool:
    """
    Checks if given id is valid
    :param id_number: the id
    :return: True if valid, False otherwise
    """
    final_lst: list[int] = [int(dig) for dig in str(id_number)]
    for x in range(1, len(final_lst), 2):
        final_lst[x] = final_lst[x] * 2

    final_lst = list(map(lambda x: sum(int(dig) for dig in str(x)), final_lst))
    return sum(final_lst) % 10 == 0


class IDIterator:
    """
    A class of an iterator generating id values
    """

    def __init__(self, id_num: int) -> None:
        """
        init function
        :param id_num: initial id number
        :return: None
        """
        self._id: int = id_num

    def __iter__(self) -> IDIterator:
        return self

    def __next__(self):
        """
        :return: the next id value in the iterator
        :raise StopIteration: raises exception when end is reached
        """
        while True:
            self._id += 1
            if self._id == MAX_ID:
                raise StopIteration
            if check_id_valid(self._id):
                return self._id


def id_generator(id_num: int) -> Generator:
    """
    Generator of id values
    :param id_num: initial id value
    :return: Generator
    """
    id_num += 1
    while id_num < MAX_ID:
        if check_id_valid(id_num):
            yield id_num
        id_num += 1


def main():
    id: int = int(input("Enter id: "))
    it_type: str = input("Generator or Iterator? (gen/it)? ")
    if it_type == "it":
        it: Iterator = iter(IDIterator(id))
    else:
        it: Generator = id_generator(id)

    for i in range(10):
        try:
            print(next(it))
        except StopIteration:
            print("end was reached")


if __name__ == '__main__':
    main()
