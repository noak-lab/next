class GreetingCard:
    """
    A class representing a greeting card
    """
    def __init__(self, recipient: str = "Dana Ev", sender: str = "Eyal Ch") -> None:
        """
        init function
        :param recipient: recipient's name
        :param sender: sender's name
        :return: None
        """
        self._recipient: str = recipient
        self._sender: str = sender

    def greeting_msg(self) -> None:
        """
        Prints cards info
        :return: None
        """
        print(f"from {self._sender} to {self._recipient}")
