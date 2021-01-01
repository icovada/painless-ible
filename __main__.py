"""
Automatic LedBuild calendar file generator
"""

from datetime import datetime as dt
from datetime import timedelta
import logging
from settings import YEAR, ANIMATIONS_OPEN, ANIMATIONS_SHIFT
from objects import Colour, Day, DayStreak
from plugin_collection import PluginCollection

logging.basicConfig(level=logging.DEBUG)


def generate_timetable():
    my_plugins = PluginCollection('plugins')
    # Create dictionary for the whole year
    yearbegin = dt(YEAR, 1, 1)
    yearend = dt(YEAR+1, 1, 1)
    curday = yearbegin

    yeardict = {}
    while curday != yearend:
        yeardict[curday] = Day(curday)
        curday = curday+timedelta(days=1)

    my_plugins.apply_all_plugins_on_value(yeardict)

    timeslotset = []
    for k, v in yeardict.items():
        thisschedule = v.get_schedule()
        if thisschedule not in timeslotset:
            timeslotset.append(thisschedule)

    colours = []
    colournum = 0
    for slot in timeslotset:
        thiscolour = Colour(colournum, slot)
        colours.append(thiscolour)
        colournum = colournum + 1

    # Since colours and timeslots are sorted the same, assign a colour to each day
    for k, v in yeardict.items():
        thisschedule = v.get_schedule()
        thiscolourindex = timeslotset.index(thisschedule)
        v.colour = colours[thiscolourindex]

    curday = yearbegin
    finalschedule = []
    while curday != yearend:
        if len(yeardict[curday].colour.timeslots) == 0:
            #Empty day
            curday = curday + timedelta(days=1)
            continue

        thisstreak = DayStreak(yeardict[curday].dt, yeardict[curday].colour)
        streakday = curday
        while yeardict[curday].colour == yeardict[streakday].colour:
            streakday = streakday + timedelta(days=1)
            if streakday == yearend:
                break

        curday = streakday
        streakday = streakday - timedelta(days=1)
        thisstreak.end = streakday
        finalschedule.append(thisstreak)

    return finalschedule

def generate_line(group, timeslotid, thisgroup, thistimeslot, animationid):
    binaryout = b''

    # Header
    if group == 0:
        binaryout += b'\x00'
    else:
        binaryout += b'\x00\x00\x00'

    # Timeslot
    binaryout += timeslotid.to_bytes(length=2, byteorder='little')

    # Colour
    binaryout += thisgroup.colour.colour.to_bytes(length=4, byteorder='little')
    binaryout += thisgroup.colour.colour.to_bytes(length=4, byteorder='little')

    # Unknown
    binaryout += b'\x00\x00\x99\x9a\x53\x00'

    # End time, m
    binaryout += thistimeslot.end[1].to_bytes(length=1, byteorder='little')

    # End time, h
    binaryout += thistimeslot.end[0].to_bytes(length=1, byteorder='little')

    # Start time, m
    binaryout += thistimeslot.begin[1].to_bytes(length=1, byteorder='little')

    # Start time, h
    binaryout += thistimeslot.begin[0].to_bytes(length=1, byteorder='little')

    # Bitmap of weekdays
    binaryout += b'\x7F'

    # End day
    binaryout += thisgroup.end.day.to_bytes(length=1, byteorder='little')

    # End month
    binaryout += thisgroup.end.month.to_bytes(length=1, byteorder='little')

    # Start day
    binaryout += thisgroup.begin.day.to_bytes(length=1, byteorder='little')

    # Start month
    binaryout += thisgroup.begin.month.to_bytes(length=1, byteorder='little')

    # Unknown
    binaryout += b'\xe5\x07'

    # Program index
    binaryout += animationid.to_bytes(length=1, byteorder='little')

    # Unknown
    binaryout += b'\x00'

    # Separator
    binaryout += b'\x1e'

    return binaryout

def save_to_binary(schedule):
    programdata = b''

    animationset = set()
    [animationset.add(x) for x in ANIMATIONS_SHIFT]
    [animationset.add(x) for x in ANIMATIONS_SHIFT]
    animationlist = list(animationset)

    for group in range(0,len(schedule)):
        thisgroup = schedule[group]
        for timeslotid in range(0,len(thisgroup.colour.timeslots)):
            thistimeslot = thisgroup.colour.timeslots[timeslotid]
            animationindex = 0
            for animation in globals()[thistimeslot.animations]:
                animationid = globals()[thistimeslot.animations].index(animation)

                programdata += generate_line(group, timeslotid, thisgroup, thistimeslot, animationid)

                animationindex = animationindex +1
    
    
    with open("calfake.bin","wb") as outfile:
        outfile.write(programdata)

    print(programdata)


if __name__ == '__main__':
    finalschedule = generate_timetable()
    save_to_binary(finalschedule)