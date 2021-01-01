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
    colour: Colour

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
        self.animations = animations


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

        aggslotlist = []
        while len(slotobjects) > 0:
            aggslot, slotobjects = self._aggregate_timeslots(slotobjects)
            aggslotlist = aggslotlist + aggslot

        return aggslotlist

    def _aggregate_timeslots(self, slotobjects: List[Timeslot]):
        """
        Recursive function to aggregate consecutive identical timeslots
        Input:
        List of timeslots, position to begin looking from
        """

        if len(slotobjects) == 1:
            return slotobjects, []

        if slotobjects[0].animations == slotobjects[1].animations and slotobjects[0].end == slotobjects[1].begin:
            aggslot = [Timeslot(slotobjects[0].begin, slotobjects[1].end, slotobjects[0].animations)]
            todolist = []
            if len(slotobjects) >= 3:
                aggslot, todolist = self._aggregate_timeslots(aggslot + slotobjects[2:])
            
            return aggslot, todolist
        
        else:
            return [slotobjects[0]], slotobjects[1:]

class DayStreak():
    begin: datetime
    end: datetime
    colour: Colour

    def __init__(self, begin, colour) -> None:
        self.begin = begin
        self.colour = colour
