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
        self.night_begin = None
        self.morning = None
        self.lunch = None
        self.afternoon = None
        self.night_end = None

    def get_schedule(self):
        schedule = [self.night_begin, self.morning, self.lunch, self.afternoon, self.night_end]

        return schedule

class Colour():
    colour: int

    def __init__(self, colour, programs) -> None:
        self.colour = colour
        self.programs = programs

class Timeslot():
    def __init__(self, begin: tuple, end: tuple) -> None:
        self.begin = begin
        self.end = end
