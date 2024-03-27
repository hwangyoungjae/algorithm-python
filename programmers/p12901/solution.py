import datetime

WEEKDAY = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]


def solution(a, b):
    return WEEKDAY[datetime.date(2016, a, b).weekday()]
