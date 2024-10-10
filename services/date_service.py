import datetime


def parse_date(date_str: str):
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
    return datetime.datetime.strptime(date_str, date_format)


def convert_time_span(date, time_span):
    match time_span.lower():
        case 'week':
            return date + datetime.timedelta(days=6)
        case 'month':
            return date + datetime.timedelta(days=29)
        case 'day':
            return date
        case _:
            return False


def convert_time(date: str):
    date_format = '%d-%m-%Y'
    return datetime.datetime.strptime(date, date_format)