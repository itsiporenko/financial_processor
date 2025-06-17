import csv
from db import PriceModifierDB
from instrument import get_instrument_processor
from utils import is_business_day, parse_date

def process_file(file_path):
    '''Processing sample_input.csv applying rules for every instrument-type'''
    db = PriceModifierDB("modifiers.db")
    instrument_processors = {}

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for instrument, date_str, value_str in reader:
            date = parse_date(date_str)
            if not is_business_day(date):
                continue
            value = float(value_str)
            multiplier = db.get_multiplier(instrument)
            adjusted_value = value * multiplier

            if instrument not in instrument_processors:
                instrument_processors[instrument] = get_instrument_processor(instrument)
            instrument_processors[instrument].add_entry(date, adjusted_value)

    for inst, processor in instrument_processors.items():
        print(f"{inst}: {processor.get_result()}")
