from datetime import datetime as dt


def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d').strftime('%d-%m-%Y')


def float_to_int(data):
    if data == '':
        return None
    else:
        return int(float(data))


def parse_Int(i):
    if i == '':
        return None
    else:
        return int(i)
