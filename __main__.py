"""
Automatic LedBuild calendar file generator
"""

from datetime import datetime as dt
from datetime import timedelta
import logging
from settings import YEAR
from objects import Colour, Day
from plugin_collection import PluginCollection

logging.basicConfig(level=logging.DEBUG)

def main():
    my_plugins = PluginCollection('plugins')
    # Create dictionary for the whole year
    yearbegin = dt(YEAR,1,1)
    yearend = dt(YEAR+1,1,1)
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
    
    print(colours)


if __name__ == '__main__':
    main()