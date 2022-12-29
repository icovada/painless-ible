"""
Automatic LedBuild calendar file generator
"""

from datetime import datetime as dt
from datetime import timedelta
import logging
from settings import YEAR, ANIMATIONS_OPEN, ANIMATIONS_SHIFT, ANIMATION_CLOSED
from objects import Colour, Day, DayStreak
from plugin_collection import PluginCollection
from iblestructs import ible_encode

logging.basicConfig(level=logging.DEBUG)


def generate_timetable():
    my_plugins = PluginCollection('plugins')
    # Create dictionary for the whole year
    yearbegin = dt(YEAR, 1, 1)
    yearend = dt(YEAR+1, 1, 1)
    curday = yearbegin

    # Fill dictionary with Day instances
    yeardict = {}
    while curday != yearend:
        yeardict[curday] = Day(curday)
        curday = curday+timedelta(days=1)

    my_plugins.apply_all_plugins_on_value(yeardict)

    # Generate set of all possible combinations of time slots for the year
    # Can't use a set() because Lists are not hashable
    timeslotset = set()
    for k, v in yeardict.items():
        thisschedule = v.get_schedule()
        timeslotset.add(thisschedule)

    # Generate a Colour for each timeslot set
    colours_assignment = {}
    colournum = 8
    for slot in timeslotset:
        colours_assignment.update({
            slot: Colour(colournum, slot)
        })
        colournum = colournum + 1

    # Since colours and timeslots are sorted the same, assign a colour to each day
    for k, v in yeardict.items():
        v.colour = colours_assignment[v.get_schedule()]

    curday = yearbegin
    finalschedule = []
    while curday != yearend:
        if len(yeardict[curday].colour.timeslots) == 0:
            # Empty day
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


def generate_struct(group, timeslotid, thisgroup, thistimeslot, animationid, firstrun):
    "Generate progrm struct"

    binaryout = ible_encode(
        group,
        timeslotid,
        thisgroup.colour.colour,
        thistimeslot.end[1],
        thistimeslot.end[0],
        thistimeslot.begin[1],
        thistimeslot.begin[0],
        thisgroup.end.day,
        thisgroup.end.month,
        YEAR,
        thisgroup.begin.day,
        thisgroup.begin.month,
        YEAR,
        animationid,
        firstrun
    )

    return binaryout


def save_to_binary(schedule):
    programdata = b''

    animationset = set()
    _ = [animationset.add(x) for x in ANIMATIONS_SHIFT]
    _ = [animationset.add(x) for x in ANIMATIONS_OPEN]
    animationlist = list(animationset)

    firstrun = True
    for group_pos, group in enumerate(schedule):
        for timeslot_pos, timeslot in enumerate(group.colour.timeslots):
            animationindex = 0
            for animation in globals()[timeslot.animations]:
                animationid = animationlist.index(animation)

                programdata += generate_struct(
                    group_pos, timeslot_pos, group, timeslot, animationid, firstrun)

                firstrun = False

                animationindex = animationindex + 1

    binary_animationlist = [x.encode('ascii') for x in animationlist]
    separator = b'\x1c'

    bin_programlist = separator.join(binary_animationlist)
    bin_programlist += b'\x1c' + ANIMATION_CLOSED.encode('ascii')
    bin_programlist += b'\x1c\x1d\x01'
    bin_programlist += len(animationlist).to_bytes(length=1,
                                                   byteorder='little')
    bin_programlist += b'\x00\x1d'

    header = b'\x50\x48\x54\x00\x00\x00\x00\x00\x31\x31\x30\x00\x00\x00\x00\x00'
    header += ('1/1/' + str(YEAR)).encode('ascii')
    header += b'\x2f\x00\x00'

    length = len(programdata) + len(bin_programlist) - 1

    with open(f"Programmazione croce/{YEAR}/calendario2020.cal", "wb") as outfile:
        outfile.write(header)
        outfile.write(length.to_bytes(length=4, byteorder='little'))
        outfile.write(b'\x1d')
        outfile.write(programdata)
        outfile.write(b'\x1d')
        outfile.write(bin_programlist)


if __name__ == '__main__':
    finalschedule = generate_timetable()
    save_to_binary(finalschedule)
