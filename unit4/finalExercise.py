from typing import Generator

SEC_IN_MIN: int = 60
MIN_IN_HOUR: int = 60
HOUR_IN_DAY: int = 24
FEB_IN_LEAP_YEAR: int = 29
MONTHS_IN_YEAR: int = 12
FEB: int = 2
DAYS_IN_MONTH: list[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def gen_secs() -> Generator:
    """
    Generates seconds in a minute
    :return: a generator containing the second
    """
    sec: int = 0
    while sec < SEC_IN_MIN:
        yield sec
        sec += 1


def gen_minutes() -> Generator:
    """
    Generates minutes in an hour
    :return: a generator containing the minute
    """
    mnts: int = 0
    while mnts < MIN_IN_HOUR:
        yield mnts
        mnts += 1


def gen_hours() -> Generator:
    """
    Generates hours in a day
    :return: a generator containing the hour
    """
    hour: int = 0
    while hour < HOUR_IN_DAY:
        yield hour
        hour += 1


def gen_time() -> Generator:
    """
    Generates the time in a day
    :return: a generator containing a string that represents the time
    """
    sec_gen: Generator[int] = gen_secs()
    mnts_gen: Generator[int] = gen_minutes()
    hours_gen: Generator[int] = gen_hours()

    sec: int = next(sec_gen)
    mnts: int = next(mnts_gen)
    hour: int = next(hours_gen)

    yield f"{hour}:{mnts}:{sec}"
    while True:
        try:
            sec = next(sec_gen)
        except StopIteration:
            try:
                sec_gen = gen_secs()
                sec = next(sec_gen)
                mnts = next(mnts_gen)
            except StopIteration:
                mnts_gen = gen_minutes()
                mnts = next(mnts_gen)
                hour = next(hours_gen)
        yield f"{hour}:{mnts}:{sec}"


def gen_years(start: int = 2019) -> Generator:
    """
    Generates a year
    :param start: the year the generator starts from
    :return: a generator containing the year
    """
    year: int = start
    while True:
        yield year
        year += 1


def gen_months() -> Generator:
    """
    Generates month in a year
    :return: a generator containing the month
    """
    month: int = 0
    while month < MONTHS_IN_YEAR:
        month += 1
        yield month


def gen_days(month: int, leap_year: bool = True) -> Generator:
    """
    Generates day in a month
    :param month: the month
    :param leap_year: whether it's a leap year or not
    :return: a generator containing the day
    """
    day: int = 1
    days: int = DAYS_IN_MONTH[month - 1]
    if month == FEB and leap_year:
        days = FEB_IN_LEAP_YEAR
    while day < days:
        yield day
        day += 1


def is_leap_year(year: int) -> bool:
    """
    Checks whether given year is a leap year or not
    :param year: the year
    :return: True if it's a leap year, false otherwise
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def gen_date() -> Generator:
    """
    Generates the date
    :return: a generator containing a string that represents the time and date
    """
    year_gen: Generator[int] = gen_years()
    month_gen: Generator[int] = gen_months()
    time_gen: Generator[str] = gen_time()

    year: int = next(year_gen)
    month: int = next(month_gen)
    day_gen = gen_days(month, is_leap_year(year))
    day: int = next(day_gen)
    time: str = next(time_gen)

    yield f"{day}/{month}/{year} " + time
    while True:
        try:
            time = next(time_gen)
        except (RuntimeError, StopIteration):
            try:
                time_gen = gen_time()
                time = next(time_gen)
                day = next(day_gen)
            except StopIteration:
                try:
                    month = next(month_gen)
                except StopIteration:
                    month_gen = gen_months()
                    month = next(month_gen)
                    year = next(year_gen)
                finally:
                    day_gen = gen_days(month, is_leap_year(year))
                    day = next(day_gen)

        finally:
            yield f"{day}/{month}/{year} " + time


def main():
    try:
        for gt in gen_time():
            print(gt)
    except RuntimeError:
        pass

    x: int = 1
    gen: Generator[str] = gen_date()
    while True:
        if x % 1000000 == 0:
            print(next(gen))
        x += 1
        try:
            next(gen)
        except StopIteration:
            pass


if __name__ == '__main__':
    main()
