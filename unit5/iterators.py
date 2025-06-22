import itertools
import winsound
from typing import Iterator
#####################  5.1.2  #####################


def play() -> None:
    """
    Plays little Yehonatan
    :return: None
    """
    freqs: dict[str, int] = {"la": 220, "si": 247, "do": 261, "re": 293, "mi": 329, "fa": 349, "sol": 392}
    notes: str = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250"
    split_notes: Iterator = iter(notes.split('-'))
    for sound in split_notes:
        note: list[str] = sound.split(',')
        winsound.Beep(freqs[note[0]], int(note[1]))


#####################  5.2.2  #####################


def print_third() -> None:
    """
    Prints every third number
    :return: None
    """
    numbers: Iterator = iter(list(range(1, 101)))
    for i in numbers:
        print(i)
        try:
            next(numbers)
            next(numbers)
        except StopIteration:
            break

#####################  5.2.3  #####################


def purse() -> None:
    """
    Finds all possible combinations that add up to 100
    :return: None
    """
    wallet: list[int] = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    counter: int = 0
    for i in range(len(wallet)):
        combinations: set = set(itertools.combinations(wallet, i))
        counter += len(set(filter(lambda x: sum(x) == 100, combinations)))
    print(counter)


def main():
    play()
    print_third()
    purse()


if __name__ == '__main__':
    main()
