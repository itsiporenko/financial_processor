import os
from processor import process_file
from db import create_price_modifier_db


def main():
    # could be replaced by any other file path for testing
    input_file = 'sample_input.csv'

    #only for test-task
    create_price_modifier_db('modifiers.db')

    if os.path.exists(input_file):
        print(f"Starting to process file: {input_file}")
        process_file(input_file)
    else:
        print(f"Error: The file {input_file} does not exist.")


if __name__ == '__main__':
    main()
