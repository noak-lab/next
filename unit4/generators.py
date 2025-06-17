################################## 4.1.2 ##################################
import itertools


def translate(sentence: str) -> str:
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    gen = (words[i] for i in sentence.split(' '))
    return ' '.join(list(gen))

################################## 4.1.3 ##################################


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n: int) -> int:
    gen = (i for i in range(n + 1, n*2 + 1) if is_prime(i))
    return gen.__next__()


################################## 4.2.2 ##################################


def parse_ranges(ranges_string):
    lst = (x.split("-") for x in ranges_string.split(","))
    g = ()
    for cell in lst:
        g = itertools.chain(g, (num for num in range(int(cell[0]), int(cell[1]) + 1)))
    return g

################################## 4.3.4 ##################################


def get_fibo():
    x = 0
    y = 1
    yield x
    yield y
    while True:
        temp = y
        y = y + x
        x = temp
        yield y
