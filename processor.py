import csv
from db import PriceModifierDB
from instrument import get_instrument_processor
from utils import is_business_day, parse_date


def read_and_sort_csv(file_path, key_field):
    """
    Reads *input_data*.csv, sorts it by date_str, returns the sorted data

    :param file_path: input_data.csv file path
    :param key_field: date_str to sort by
    :return: Sorted list of rows
    """
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        sorted_rows = sorted(reader, key=lambda row: row[key_field])
    return sorted_rows


def process_in_chunks(file_path, chunk_size, key_field, instrument_processors, db):
    """
    Processes a huge *input-data*.csv in chunks, sorting each chunk by 'date_str'(key-field) to avoid memory overload

    :param file_path: path to *input_data*.csv
    :param chunk_size: rows-number per chunk
    :param key_field: date_str for sorting
    :param instrument_processors: dictionary for instruments mapping
    :param db: instance of Class PriceModifierDB
    """
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        fieldnames = ['instrument', 'date_str', 'value_str']
        reader = csv.DictReader(file, fieldnames=fieldnames)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) >= chunk_size:
                # Process and sort the chunk before continuing
                sorted_chunk = sorted(chunk, key=lambda row: row[key_field])
                process_chunk(sorted_chunk, instrument_processors, db)
                chunk = []  # clear the chunk to free memory
        # process rested rows in the last chunk
        if chunk:
            sorted_chunk = sorted(chunk, key=lambda row: row[key_field])
            process_chunk(sorted_chunk, instrument_processors, db)


def process_chunk(chunk, instrument_processors, db):
    """
    Processes a single chunk of sorted data.

    :param chunk: list of sorted-rows
    :param instrument_processors: dictionary instruments mapping
    :param db: instance for PriceModifierDB
    """
    for row in chunk:
        instrument = row['instrument']
        date_str = row['date_str']
        value_str = row['value_str']

        # parse the date and ensure it's a business day
        date = parse_date(date_str)
        if not is_business_day(date):
            continue

        # base logic: convert value_str to float and adjust with multiplier
        value = float(value_str)
        multiplier = db.get_multiplier(instrument)
        adjusted_value = value * multiplier

        # Get or create the instrument processor
        if instrument not in instrument_processors:
            instrument_processors[instrument] = get_instrument_processor(instrument)

        # Add the adjusted value for the given instrument
        instrument_processors[instrument].add_entry(date, adjusted_value)


def process_file(file_path):
    """
    Processing *input_data*.csv(sample_input.csv) applying rules for every instrument-type

    :param file_path: path to *input_data*.csv
    """
    # Initialize the PriceModifierDB instance
    db = PriceModifierDB("modifiers.db")
    instrument_processors = {}

    # field for sorting --> 'date_str'
    key_field = 'date_str'

    # process file in chunks
    process_in_chunks(file_path, chunk_size=1000, key_field=key_field, instrument_processors=instrument_processors,
                      db=db)

    # print the results in the desired format
    results = {}
    for inst, processor in instrument_processors.items():
        results[inst] = processor.get_result()

    # sort the results by instrument name
    sorted_results = {k: v for k, v in sorted(results.items())}

    for inst, result in sorted_results.items():
        print(f"{inst}: {result}")