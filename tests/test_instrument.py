from datetime import datetime
from instrument import Instrument1, Instrument2, Instrument3, GenericInstrument

def test_instrument1_mean():
    instr = Instrument1()
    instr.add_entry(datetime(2020, 1, 1), 10)
    instr.add_entry(datetime(2020, 1, 2), 20)
    assert abs(instr.get_result() - 15.0) < 1e-6

def test_instrument2_nov_2014():
    instr = Instrument2()
    instr.add_entry(datetime(2014, 11, 1), 10)
    instr.add_entry(datetime(2014, 10, 1), 20)
    assert instr.get_result() == 10

def test_instrument3_variance():
    instr = Instrument3()
    for val in [2, 4, 4, 4, 5, 5, 7, 9]:
        instr.add_entry(datetime(2020, 1, 1), val)
    assert round(instr.get_result(), 2) == 4.0

def test_generic_instrument():
    instr = GenericInstrument()
    for i in range(20):
        instr.add_entry(datetime(2020, 1, i+1), i)
    assert instr.get_result() == sum(range(10, 20))
