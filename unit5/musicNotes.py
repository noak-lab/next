from __future__ import annotations
from typing import Iterator


class MusicNotes:
    """
    A class of an iterator generating notes
    """

    def __init__(self) -> None:
        """
        init function
        :return: None
        """
        self._OCT_NUM: int = 5
        self._freq_list: list[int] = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self._octave: int = 0
        self._note_index: int = 0

    def __iter__(self) -> MusicNotes:
        return self

    def __next__(self) -> int:
        """
        :return: the next note's frequency in the iterator
        :raise StopIteration: raises exception when end is reached
        """
        if self._note_index == len(self._freq_list):
            if self._octave + 1 >= self._OCT_NUM:
                raise StopIteration
            self._note_index = 1
            self._octave += 1
        else:
            self._note_index += 1
        return self._freq_list[self._note_index - 1] * (2 ** self._octave)


def main():
    notes_iter: MusicNotes = MusicNotes()
    for freq in notes_iter:
        print(freq)


if __name__ == '__main__':
    main()
