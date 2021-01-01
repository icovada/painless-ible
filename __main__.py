"""
Automatic LedBuild calendar file generator
"""

from datetime import datetime as dt
from datetime import timedelta
import logging
from settings import YEAR, SHIFT_DURATION, FIRST_SHIFT_BEGIN, SHIFT_ROTATION_DAYS
from objects import Day
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

    return my_plugins


if __name__ == '__main__':
    main()

## Colour all non-holidays as working days
#for k, v in yeardict.items():
#    if not v.holiday:
#        v.colour = col_shiftbegin
#
## Colour all mondays as mondays
#for k, v in yeardict.items():
#    if not v.holiday:
#        if v.dt.isoweekday == 1:
#            v.colour = col_monday
#
#for k, v in yeardict.items():
#    if v.shift == "begin":
#        v.colour = col_shiftbegin
#    elif v.shift == "day":
#        v.colour = col_shiftday
#    elif v.shift == "end":
#        if v.holiday:
#            v.colour = col_shiftendholiday
#        else:
#            v.colour = col_shiftend
#
#[val.colour for key, val in yeardict.items()]