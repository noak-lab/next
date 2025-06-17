from typing import Generator
################################## 4.1.2 ##################################


def translate(sentence: str) -> str:
    """
    translates a sentence from spanish to english
    :param sentence: original sentence
    :return: the translated sentence
    """
    words: dict[str, str] = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    gen: Generator[str] = (words[i] for i in sentence.split(' '))
    return ' '.join(list(gen))

################################## 4.1.3 ##################################


def is_prime(n: int) -> bool:
    """
    checks if n is a prime number
    :param n: the number
    :return: True if prime, false otherwise
    """
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n: int) -> int:
    """
    returns the first prime number that's bigger than n
    :param n: base number
    :return: the prime number
    """
    gen: Generator[int] = (i for i in range(n + 1, n*2 + 1) if is_prime(i))
    return next(gen)


################################## 4.2.2 ##################################


def parse_ranges(ranges_string: str) -> Generator:
    """
    receives a list of ranges and return a generator containing all the number within those ranges
    :param ranges_string: the string containing the ranges
    :return: generator af all the numbers
    """
    range_list: Generator[list[str]] = (x.split("-") for x in ranges_string.split(","))
    return (num for cell in range_list for num in range(int(cell[0]), int(cell[1]) + 1))

################################## 4.3.4 ##################################


def get_fibo() -> Generator:
    """
    :return: a generator containing a number from the fibonacci sequence
    """
    x: int = 0
    y: int = 1
    yield x
    yield y
    while True:
        temp = y
        y = y + x
        x = temp
        yield y


def main():
    print(translate("el gato esta en la casa"))
    print(first_prime_over(1000000))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))

    fibo_gen = get_fibo()
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))


if __name__ == '__main__':
    main()