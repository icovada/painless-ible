from datetime import date, datetime
from typing import List
from holidays import allholidays

class Colour():
    pass
class Day():
    holiday: bool
    shift: List[str]
    dt: datetime
    colour: Colour

    def __init__(self, dt) -> None:
        self.dt = dt
        if dt in allholidays or dt.isoweekday() == 7:
            self.holiday = True
        else:
            self.holiday = False

        self.shift = None
        self.colour = None


class Program():
    begin: tuple
    end: tuple
    programs: list

    def __init__(self, begin, end, programs) -> None:
        self.begin = begin
        self.end = end
        self.programs = programs

class Colour():
    colour: int
    programs: List[Program]

    def __init__(self, colour, programs) -> None:
        self.colour = colour
        self.programs = programs