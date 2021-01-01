from datetime import date, datetime
from settings import ANIMATIONS_OPEN, ANIMATIONS_SHIFT, TIME_NIGHT_BEGIN, TIME_MORNING, TIME_LUNCH, TIME_AFTERNOON, TIME_NIGHT_END
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

class Timeslot():
    """
    Defines animation timeslot with begin, end and animation list
    """
    def __init__(self, begin: tuple, end: tuple, animations: str) -> None:
        self.begin = begin
        self.end = end
        if animations is not None:
            self.animations = globals()[animations]
        else:
            self.animations = None

class Colour():
    colour: int
    timeslots: List[Timeslot]

    def __init__(self, colour, timeslots) -> None:
        self.colour = colour
        self.timeslots = self._parse_timeslots(timeslots)

    def _parse_timeslots(self, timeslots: str) -> list:
        assert len(timeslots) == 5

        slotobjects = []

        if timeslots[0] is not None:
            thisslot = Timeslot(*TIME_NIGHT_BEGIN, timeslots[0])
            slotobjects.append(thisslot)

        if timeslots[1] is not None:
            thisslot = Timeslot(*TIME_MORNING, timeslots[1])
            slotobjects.append(thisslot)

        if timeslots[2] is not None:
            thisslot = Timeslot(*TIME_LUNCH, timeslots[2])
            slotobjects.append(thisslot)

        if timeslots[3] is not None:
            thisslot = Timeslot(*TIME_AFTERNOON, timeslots[3])
            slotobjects.append(thisslot)

        if timeslots[4] is not None:
            thisslot = Timeslot(*TIME_NIGHT_END, timeslots[4])
            slotobjects.append(thisslot)

        return slotobjects