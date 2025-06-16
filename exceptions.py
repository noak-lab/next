def stop_iteration_err() -> None:
    """
    raises StopIteration error
    """
    l = iter("hh")
    while True:
        next(l)

def division_by_zero_err() -> None:
    """
    raises ZeroDivisionError error
    """
    l: int = 4 / 0


def assertion_err() -> None:
    """
    raises AssertionError error
    """
    assert 3 > 4


def import_err() -> None:
    """
    raises ImportError error
    """
    from math import hhhh


def key_err() -> None:
    """
    raises KeyError error
    """
    dict = {"s": "j"}
    dict["f"]


def sytax_err() -> None:
    """
    raises SyntaxError error
    """
    l = {"g": "g" "h": "g"}


def indentation_err() -> None:
    """
    raises IndentationError error
    """
print("xxx")


def type_err() -> None:
    """
    raises TypeError error
    """
    l = 'w' + 4