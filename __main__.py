"""
Automatic LedBuild calendar file generator
"""

from datetime import datetime as dt, timedelta
import json

with open("animations.config", "r") as animationsfile:
    ANIMATIONS = json.loads(animationsfile)

with open("colours.config", "r") as coloursfile:
    COLOURS = json.loads(coloursfile)

with open("calendar.config", "r") as calendarfile:
    CALENDAR = json.loads(calendarfile)

assert "default" in ANIMATIONS.keys()

DEFAULTANIMATION = ANIMATIONS.pop("default")

BASEDATE = dt(year=CALENDAR["year"],
              month=CALENDAR["month"],
              day=CALENDAR["day"])
ENDDATE = dt(year=CALENDAR["year"] + 1,
             month=CALENDAR["month"],
             day=CALENDAR["day"])

ANIMATIONLIST = [BASEDATE + timedelta(days=x) for x in range(0, (ENDDATE - BASEDATE).days)]

for i, j in ANIMATIONS.items():
    for k in j:
        if k not in ANIMATIONLIST:
            ANIMATIONLIST.append(k)


# Header
HEADER1 = bytearray([0x50, 0x48, 0x54, 0x00, 0x00, 0x00, 0x00,
                     0x00, 0x31, 0x31, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00])
HEADER2 = bytearray(
    "1/{}/{}/".format(CALENDAR["year"], CALENDAR["month"]), "ascii")
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


OUTPUTFILE.close()
