from file1 import GreetingCard


class BirthdayCard(GreetingCard):
    def __init__(self, recipient: str = "Dana Ev", sender: str = "Eyal Ch", sender_age: int = 0):
        GreetingCard().__init__(recipient, sender)
        self._sender_age: int = sender_age

    def greeting_msg(self):
        GreetingCard().greeting_msg()
        print(f"Happy Birthday, sender's age: {self._sender_age}")


