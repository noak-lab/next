import string
import finalExercise.exceptions as exceptions

MIN_USERNAME_LEN = 3
MAX_USERNAME_LEN = 16
MIN_PASSWORD_LEN = 8
MAX_PASSWORD_LEN = 40


def check_intput(username: str, password: str) -> None:
    """
    checks if users credentials are valid
    :param username: user's username
    :param password: user's password
    :return: None
    """
    try:
        if check_username(username):
            if check_password(password):
                print("OK")
    except Exception as err:
        raise err


def check_password(password: str) -> bool:
    """
    checks password's validity
    :param password: password
    :return: True id valid, raises exception otherwise
    """
    if len(password) < MIN_PASSWORD_LEN:
        raise exceptions.PasswordTooShort
    if len(password) > MAX_PASSWORD_LEN:
        raise exceptions.PasswordTooLong

    return check_characters(password)


def check_characters(password: str) -> bool:
    """
    checks all character requirements for passsword
    :param password: password
    :return: True if valid, raises exception otherwise
    """
    uppercase_flag: bool = False
    lowercase_flag: bool = False
    digit_flag: bool = False
    symbol_flag: bool = False

    for chr in password:
        if not digit_flag:
            digit_flag = chr.isdigit()
        if chr.isalpha():
            if not uppercase_flag or not lowercase_flag:
                if chr.isupper():
                    uppercase_flag = True
                elif not lowercase_flag:
                    lowercase_flag = True
        if not symbol_flag:
            symbol_flag = chr in string.punctuation

    if not symbol_flag:
        raise exceptions.PasswordMissingSpecial
    if not lowercase_flag:
        raise exceptions.PasswordMissingLowerCase
    if not uppercase_flag:
        raise exceptions.PasswordMissingUpperCase
    if not digit_flag:
        raise exceptions.PasswordMissingDigit

    return True


def check_username(username: str) -> bool:
    """
    checks if username is valid
    :param username: username
    :return: True if valid, raises exceptions otherwise
    """
    if len(username) < MIN_USERNAME_LEN:
        raise exceptions.UsernameTooShort
    if len(username) > MIN_USERNAME_LEN:
        raise exceptions.UsernameTooLong

    for i in range(len(username)):
        if not username[i].isalpha() and not username[i].isdigit() and username[i] != '_':
            raise exceptions.UsernameContainsIllegalCharacter(i, username[i])

    return True
