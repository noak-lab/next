class GreetingCard:
    def __init__(self, recipient: str = "Dana Ev", sender: str = "Eyal Ch"):
        self._recipient: str = recipient
        self._sender: str = sender

    def greeting_msg(self):
        print(f"from {self._sender} to {self._recipient}")
