import sqlite3
import os
from db import PriceModifierDB

def setup_test_db(path):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS INSTRUMENT_PRICE_MODIFIER (ID INTEGER PRIMARY KEY, NAME TEXT, MULTIPLIER REAL)")
    cur.execute("INSERT INTO INSTRUMENT_PRICE_MODIFIER (NAME, MULTIPLIER) VALUES ('INSTRUMENT1', 2.0)")
    conn.commit()
    conn.close()

def test_get_multiplier(tmp_path):
    db_path = tmp_path / "test.db"
    setup_test_db(db_path)
    db = PriceModifierDB(str(db_path))
    assert db.get_multiplier("INSTRUMENT1") == 2.0
    assert db.get_multiplier("UNKNOWN") == 1.0
