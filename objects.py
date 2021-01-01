from datetime import date, datetime
from typing import List
from holidays import allholidays

class Colour():
    pass
class Day():
    holiday: bool
    shift: List[str]
    dt: datetime

    def __init__(self, dt) -> None:
        self.dt = dt
        if dt in allholidays or dt.isoweekday() == 7:
            self.holiday = True
        else:
            self.holiday = False

        self.shift = None
        self.schedule = []

class Colour():
    colour: int

    def __init__(self, colour, programs) -> None:
        self.colour = colour
        self.programs = programs

class Timeslot():
    def __init__(self, begin: tuple, end: tuple) -> None:
        self.begin = begin
        self.end = end
