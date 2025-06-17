# Financial Processor 

## How to Run 
```
bash pip install -r requirements.txt 
bash run.sh 
```

## Project structure
```
financial_processor/
├── main.py                      # Entry point
├── processor.py                 # Line reader, controller
├── instrument.py                # Instrument classes & strategy logic
├── db.py                        # DB access and caching
├── utils.py                     # Utility functions (e.g., business date check)
├── requirements.txt             # All dependencies
├── run.bat                      # Windows batch script to run the program
├── test/
│   ├── test_instrument.py       # Unit tests for instruments
│   ├── test_utils.py            # Unit tests for utilities
│   └── test_db                  # Unit tests for db-connection
├── task/
│   ├── example_input.txt        # Instruments-prices input sample(*.csv)
│   ├── task1.txt                # Test task description
└── sample_input.csv             # Input CSV file (or path to large file)
```

## Instrument's price calculation rules
 - INSTRUMENT1: Mean of all prices
 - INSTRUMENT2: Mean for Nov 2014
 - INSTRUMENT3: Minimum price seen
 - Other instruments: Sum of latest 10 values

## How to Run Tests
```
  bash pytest tests/ 
```

## Design Highlights
 - Efficient memory usage (streaming)
 - Caching DB access with 5s TTL
 - Modular OO design for instrument behavior
 - SQLite file-based DB (portable)
