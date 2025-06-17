def gen_secs():
    sec = 0
    while sec < 60:
        yield sec
        sec += 1


def gen_minutes():
    mnts = 0
    while mnts < 60:
        yield mnts
        mnts += 1


def gen_hours():
    hour = 0
    while hour < 24:
        yield hour
        hour += 1


def gen_time():
    end_of_clock = False
    sec_gen = gen_secs()
    mnts_gen = gen_minutes()
    hours_gen = gen_hours()

    sec = sec_gen.__next__()
    mnts = mnts_gen.__next__()
    hour = hours_gen.__next__()

    yield f"{hour}:{mnts}:{sec}"
    while not end_of_clock:
        try:
            sec = sec_gen.__next__()
        except StopIteration:
            try:
                sec_gen = gen_secs()
                sec = sec_gen.__next__()
                mnts = mnts_gen.__next__()
            except StopIteration:
                mnts_gen = gen_minutes()
                mnts = mnts_gen.__next__()
                hour = hours_gen.__next__()

        finally:
            yield f"{hour}:{mnts}:{sec}"


def gen_years(start=2019):
    year = start
    while True:
        yield year
        year += 1


def gen_months():
    month = 1
    while month < 13:
        yield month
        month += 1


def gen_days(month, leap_year=True):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 1
    days = months[month]
    if month == 2 and leap_year:
        days = 29
    while day < days:
        yield day
        day += 1


def is_leap_year(year: int):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def gen_date():
    year_gen = gen_years()
    month_gen = gen_months()
    time_gen = gen_time()

    year = year_gen.__next__()
    month = month_gen.__next__()
    day_gen = gen_days(month, is_leap_year(year))
    day = day_gen.__next__()
    time = time_gen.__next__()

    yield f"{day}/{month}/{year} " + time
    while True:
        try:
            time = time_gen.__next__()
        except RuntimeError or StopIteration:
            try:
                time_gen = gen_time()
                time = time_gen.__next__()
                day = day_gen.__next__()
            except StopIteration:
                try:
                    month = month_gen.__next__()
                except StopIteration:
                    month_gen = gen_months()
                    month = month_gen.__next__()
                    year = year_gen.__next__()
                finally:
                    day_gen = gen_days(month, is_leap_year(year))
                    day = day_gen.__next__()

        finally:
            yield f"{day}/{month}/{year} " + time


def main():
    try:
        for gt in gen_time():
            print(gt)
    except RuntimeError:
        pass

    x = 1
    gen = gen_date()
    while True:
        if x % 1000000 == 0:
            print(gen.__next__())
        x += 1
        try:
            gen.__next__()
        except StopIteration:
            pass
