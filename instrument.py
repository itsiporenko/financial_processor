from collections import deque
from statistics import mean
import heapq

class BaseInstrument:
    """
    A class to represent an Instrument.

    ...

    Methods
    -------
    add_entry(self, date, value):
        add into list instruments.
    get_result(self):
        get calculated result.
    """
    def add_entry(self, date, value):
        raise NotImplementedError
    def get_result(self):
        raise NotImplementedError

class Instrument1(BaseInstrument):
    """
    A class to represent an Instrument1.

    ...

    Attributes
    ----------
    value : list
        list of Instrument1

    Methods
    -------
    add_entry(self, date, value):
        add into list Instruments1.
    get_result(self):
        get mean(avg) result.
    """
    def __init__(self):
        self.values = []

    def add_entry(self, date, value):
        self.values.append(value)

    def get_result(self):
        return mean(self.values)

class Instrument2(BaseInstrument):
    def __init__(self):
        self.values = []

    def add_entry(self, date, value):
        if date.month == 11 and date.year == 2014:
            self.values.append(value)

    def get_result(self):
        return mean(self.values) if self.values else None

class Instrument3(BaseInstrument):
    def __init__(self):
        self.n = 0
        self.mean = 0
        self.M2 = 0

    def add_entry(self, date, value):
        self.n += 1
        delta = value - self.mean
        self.mean += delta / self.n
        delta2 = value - self.mean
        self.M2 += delta * delta2

    def get_result(self):
        return self.M2 / self.n if self.n else 0

class GenericInstrument(BaseInstrument):
    def __init__(self):
        self.heap = []

    def add_entry(self, date, value):
        heapq.heappush(self.heap, (-date.timestamp(), value))

    def get_result(self):
        top_10 = heapq.nsmallest(10, self.heap)
        return sum(val for _, val in top_10)

def get_instrument_processor(name):
    if name == "INSTRUMENT1":
        return Instrument1()
    elif name == "INSTRUMENT2":
        return Instrument2()
    elif name == "INSTRUMENT3":
        return Instrument3()
    else:
        return GenericInstrument()
