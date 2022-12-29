from settings import YEAR
from datetime import datetime as dt
from datetime import timedelta
from dateutil.easter import easter

fixed_holidays = [dt(YEAR, 1, 1),
                  dt(YEAR, 1, 6),
                  dt(YEAR, 4, 25),
                  dt(YEAR, 5, 1),
                  dt(YEAR, 6, 2),
                  dt(YEAR, 6, 24),
                  dt(YEAR, 8, 15),
                  dt(YEAR, 9, 1),
                  dt(YEAR, 12, 8),
                  dt(YEAR, 12, 25),
                  dt(YEAR, 12, 26),
                  easter(YEAR)+timedelta(days=1),
                  easter(YEAR)]

arbitrary_holidays = [dt(YEAR, 1, 7),
                      dt(YEAR, 4, 29),
                      dt(YEAR, 7, 3),
                      dt(YEAR, 7, 4),
                      dt(YEAR, 7, 5),
                      dt(YEAR, 7, 6),
                      dt(YEAR, 7, 7),
                      dt(YEAR, 7, 8),
                      dt(YEAR, 8, 28),
                      dt(YEAR, 8, 29),
                      dt(YEAR, 8, 30),
                      dt(YEAR, 8, 31),
                      dt(YEAR, 9, 1),
                      dt(YEAR, 9, 2),
                      dt(YEAR, 12, 27),
                      dt(YEAR, 12, 28),
                      dt(YEAR, 12, 29),
                      ]

allholidays = fixed_holidays + arbitrary_holidays
