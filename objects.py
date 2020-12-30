from datetime import date, datetime
from typing import List
from holidays import allholidays

class Day():
    holiday: bool
    shift: bool
    dt: datetime

    def __init__(self, dt):
        self.dt = dt
        if dt in allholidays or dt.isoweekday() == 7:
            self.holiday = True
        else:
            self.holiday = False
        
        shift = False