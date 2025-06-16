class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, index: int, char: str) -> None:
        """
        init function
        :param index: illegal chars index
        :param char: the illegal char
        """
        self._index: int = index
        self._char: str = char

    def __str__(self) -> str:
        return f"The username contains an illegal character {self._char} at index {self._index}"


class UsernameTooShort(Exception):
    def __str__(self) -> str:
        return "The username is too short "


class UsernameTooLong(Exception):
    def __str__(self) -> str:
        return "The username is too long "


class PasswordMissingCharacter(Exception):
    def __str__(self) -> str:
        return "The password is missing a character "


class PasswordTooShort(Exception):
    def __str__(self) -> str:
        return "The password is too short "


class PasswordTooLong(Exception):
    def __str__(self) -> str:
        return "The password is too long "


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self) -> str:
        return PasswordMissingCharacter.__str__(self) + "(Digit)"


class PasswordMissingUpperCase(PasswordMissingCharacter):
    def __str__(self) -> str:
        return PasswordMissingCharacter.__str__(self) + "(Uppercase)"


class PasswordMissingLowerCase(PasswordMissingCharacter):
    def __str__(self) -> str:
        return PasswordMissingCharacter.__str__(self) + "(Lowercase)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self) -> str:
        return PasswordMissingCharacter.__str__(self) + "(Special)"
