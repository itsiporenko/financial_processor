from processor import process_file
from db import create_price_modifier_db

if __name__ == "__main__":
    '''Entry point'''
    create_price_modifier_db('modifiers.db')
    process_file("sample_input.csv")
