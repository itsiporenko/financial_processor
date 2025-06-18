from datetime import datetime
from utils import parse_date, is_business_day

def test_parse_date():
    date = parse_date("12-Mar-2015")
    assert date == datetime(2015, 3, 12)

def test_is_business_day():
    assert is_business_day(datetime(2025, 6, 13))  # Friday
    assert not is_business_day(datetime(2025, 6, 14))  # Saturday
