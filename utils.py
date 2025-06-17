from datetime import datetime
import calendar

def parse_date(date_str):
    '''Parsing date function'''
    return datetime.strptime(date_str, "%d-%b-%Y")

def is_business_day(date):
    '''Check if data is a business date'''
    return calendar.weekday(date.year, date.month, date.day) < 5
