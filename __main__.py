"""
Automatic LedBuild calendar file generator
"""

from datetime import datetime as dt, timedelta
import json
import logging

logging.basicConfig(level=logging.DEBUG)

with open("animations.config", "r") as animationsfile:
    ANIMATIONS = json.load(animationsfile)

with open("colours.config", "r") as coloursfile:
    COLOURS = json.load(coloursfile)

with open("calendar.config", "r") as calendarfile:
    CALENDAR = json.load(calendarfile)

assert "default" in ANIMATIONS.keys()

DEFAULTANIMATION = ANIMATIONS.pop("default")
ANIMATIONLIST = []

BASEDATE = dt(year=CALENDAR["year"],
              month=CALENDAR["month"],
              day=1)
ENDDATE = dt(year=CALENDAR["year"] + 1,
             month=CALENDAR["month"],
             day=1)

YEAR = CALENDAR["year"]

SCHEDULE = {}

# SCHEDULE = {(BASEDATE + timedelta(days=x)):None for x in range(0, (ENDDATE - BASEDATE).days}
for x in range(0, (ENDDATE - BASEDATE).days):
    SCHEDULE[BASEDATE + timedelta(days=x)] = None

for i, j in ANIMATIONS.items():
    for k in j:
        if k not in ANIMATIONLIST:
            ANIMATIONLIST.append(k)

ANIMATIONLIST.append(DEFAULTANIMATION)


# Header
HEADER1 = bytearray([0x50, 0x48, 0x54, 0x00, 0x00, 0x00, 0x00,
                     0x00, 0x31, 0x31, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00])
HEADER2 = "1/{}/{}/".format(CALENDAR["month"],CALENDAR["year"]).encode("ascii")
HEADER3 = bytearray([0x00, 0x00, 0xD9, 0x00, 0x00, 0x00])
FIELDSEPARATOR = 0x1D

OUTPUTFILE = open("out.pnl", "wb")
OUTPUTFILE.write(HEADER1)
OUTPUTFILE.write(HEADER2)
OUTPUTFILE.write(HEADER3)


def findday(datetime, isoweekday):
    """
    Find the next monday/tuesday etc
    starting from datetime
    """
    assert 1 <= isoweekday <= 7, "Days go from 1 to 7"
    while dt.isoweekday(datetime) != isoweekday:
        datetime = datetime + timedelta(days=1)
    return datetime


def calendarfill():
    for schedule in CALENDAR["scheduling"]:
        for occurrence in schedule.values():
            for repetition in occurrence:
                start = dt(year=YEAR,
                           month=repetition["begins-month"],
                           day=repetition["begins-day"])
                for i in range(0, repetition["repeats-for"]):
                    repeatsevery = repetition["repeats-every"] if "repeats-every" in repetition else 0
                    dayseries = i
                    offset= 0
                    for j in CALENDAR["templates"][list(schedule)[0]]:
                        targetdate = start + timedelta(days=dayseries*repeatsevery+offset)
                        SCHEDULE[targetdate] = j
                        offset = offset + 1

calendarfill()

print(SCHEDULE)

OUTPUTFILE.close()
