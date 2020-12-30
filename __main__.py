"""
Automatic LedBuild calendar file generator
"""

from datetime import datetime as dt
from datetime import timedelta
import logging
from settings import YEAR, SHIFT_DURATION, FIRST_SHIFT_BEGIN, SHIFT_ROTATION_DAYS
from scheduling import col_monday, col_work_day, col_shiftbegin, col_shiftday, col_shiftend, col_shiftendholiday
from objects import Day

logging.basicConfig(level=logging.DEBUG)

# Create dictionary for the whole year
yearbegin = dt(YEAR,1,1)
yearend = dt(YEAR+1,1,1)
curday = yearbegin

yeardict = {}
while curday != yearend:
    yeardict[curday] = Day(curday)
    if curday >= FIRST_SHIFT_BEGIN:
        shift_delta = (curday-FIRST_SHIFT_BEGIN).days
        if shift_delta % SHIFT_ROTATION_DAYS == 0:
            yeardict[curday].shift = "begin"
        elif shift_delta % SHIFT_ROTATION_DAYS > 0 and shift_delta % SHIFT_ROTATION_DAYS < 7:
            yeardict[curday].shift = "day"
        elif shift_delta % SHIFT_ROTATION_DAYS == 7:
            yeardict[curday].shift = "end"

    curday = curday+timedelta(days=1)


# Colour all non-holidays as working days
for k, v in yeardict.items():
    if not v.holiday:
        v.colour = col_shiftbegin

# Colour all mondays as mondays
for k, v in yeardict.items():
    if not v.holiday:
        if v.dt.isoweekday == 1:
            v.colour = col_monday

for k, v in yeardict.items():
    if v.shift == "begin":
        v.colour = col_shiftbegin
    elif v.shift == "day":
        v.colour = col_shiftday
    elif v.shift == "end":
        if v.holiday:
            v.colour = col_shiftendholiday
        else:
            v.colour = col_shiftend

[val.colour for key, val in yeardict.items()]