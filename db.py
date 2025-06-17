import sqlite3
import time

def create_price_modifier_db(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Create the table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS INSTRUMENT_PRICE_MODIFIER (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL UNIQUE,
            MULTIPLIER REAL NOT NULL
        )
    ''')

    conn.commit()

    #only for test-purpose
    #cur.execute("INSERT OR REPLACE INTO INSTRUMENT_PRICE_MODIFIER (NAME, MULTIPLIER) VALUES (?, ?)",
    #               ("INSTRUMENT1", 1.14))
    #cur.execute("INSERT OR REPLACE INTO INSTRUMENT_PRICE_MODIFIER (NAME, MULTIPLIER) VALUES (?, ?)",
    #               ("INSTRUMENT3", 0.89))
    #conn.commit()

    conn.close()

class PriceModifierDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.cache = {}
        self.last_refresh = 0

    def get_multiplier(self, name):
        current = time.time()
        if current - self.last_refresh > 5:
            self.refresh_cache()
            self.last_refresh = current
        return self.cache.get(name, 1.0)

    def refresh_cache(self):
        self.cache.clear()
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT NAME, MULTIPLIER FROM INSTRUMENT_PRICE_MODIFIER")
        for name, mult in cur.fetchall():
            self.cache[name] = mult
        conn.close()
