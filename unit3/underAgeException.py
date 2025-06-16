class UnderAge(BaseException):
    def __init__(self, age):
        """
        init function
        :param age: underage person's age
        """
        self._age = age

    def __str__(self) -> str:
        return f"You're under age, you can attend in {18 - self._age} years"
