import underAgeException
########################## 3.1.3 ##########################
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

########################## 3.2.5 ##########################


def read_file(file_name: str) -> str:
    """
    open and reads file
    :param file_name: path to file
    :return: files content
    """
    string: str = "__CONTENT_START__\n"
    try:
        file = open(file_name, 'r')
        string += file.read() + "\n"
        file.close()
    except FileNotFoundError:
        string += "__NO_SUCH_FILE__\n"
    finally:
        string += "__CONTENT_END__\n"
        return string


########################## 3.2.5 ##########################

def send_invitation(name: str, age: int) -> None:
    """
    sends an invitation to all adults
    :param name: invitee's name
    :param age: invitee's age
    :return: None, raises exception if they're underage
    """
    if int(age) < 18:
        raise underAgeException.UnderAge(age)
    else:
        print("You should send an invite to " + name)