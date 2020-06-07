import datetime


def add(moment):
    gigasecond = 10**9
    return moment + datetime.timedelta(seconds=gigasecond)
