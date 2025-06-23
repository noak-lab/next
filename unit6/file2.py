from file1 import GreetingCard


class BirthdayCard(GreetingCard):
    """
    A class representing a birthday card
    """
    def __init__(self, recipient: str = "Dana Ev", sender: str = "Eyal Ch", sender_age: int = 0):
        """
        init function
        :param recipient: recipient's name
        :param sender: sender's name
        :param sender_age: sender's age
        :return: None
        """
        GreetingCard().__init__(recipient, sender)
        self._sender_age: int = sender_age

    def greeting_msg(self) -> None:
        """
        Prints cards info
        :return: None
        """
        GreetingCard().greeting_msg()
        print(f"Happy Birthday, sender's age: {self._sender_age}")


