from unit3 import exceptions, underAgeException
import unit3.finalExercise.credentialsChecker


def main():

    try:
        exceptions.send_invitation("nm", 20)
        exceptions.send_invitation("nm", 17)
    except underAgeException.UnderAge as err:
        print(err)
    valid_input: bool = False

    while not valid_input:
        username: str = input("Please enter your username: ")
        password: str = input("Please enter your password: ")
        try:
            unit3.finalExercise.credentialsChecker.check_intput(username, password)
            valid_input = True
        except Exception as err:
            print(err)


if __name__ == '__main__':
    main()

