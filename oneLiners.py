import functools
############################################## 1.1 ##############################################


def double_letter(my_str):
    """
    doubles each letter in given str
    :param my_str: original string
    :return: doubled string
    """
    return functools.reduce(lambda x, y: x + y + y, my_str, "")


def four_dividers(number):
    """
    returns a list of all numbers that are derivative by four between 1 and a given number
    :param number: the given number
    :return: list of all the numbers
    """
    return list(filter(lambda num: num % 4 == 0, range(1, number + 1)))


def sum_of_digits(number):
    """
    sums the value of all the digits in a number
    :param number: original number
    :return: the sum
    """
    return functools.reduce(lambda x, y: int(x) + int(y), str(abs(number)), 0)

############################################## 1.3 ##############################################


def intersection(list_1, list_2):
    """
    finds the intersection of two given lists
    :param list_1: first list
    :param list_2: second list
    :return: a list of all shared numbers
    """
    return list(set([x for x in list_1 if x in list_2]))


def is_prime(number):
    """
    checks if given number is a prime number
    :param number: given number
    :return: true if prime false otherwise
    """
    return functools.reduce(lambda x, y: x and y, [True if number % x != 0 else False for x in range(2, number)])


def is_funny(string):
    """
    checks if all chars in string are a or h
    :param string: original string
    :return: true if string is only made up of h and a, false otherwise
    """
    return functools.reduce(lambda x, y: x and y, [True if x == 'h' or x == 'a' else False for x in string])


def decrypt_password(password):
    """
    decrypts given password, caeser cipher
    :param password: original encrypted password
    :return: password after decryption
    """
    return functools.reduce(lambda x, y: x + y, [chr(2 + ord(x)) if x.isalpha() else x for x in password])
