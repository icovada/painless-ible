from settings import YEAR
from datetime import datetime as dt
from datetime import timedelta
from dateutil.easter import easter

fixed_holidays = [dt(YEAR,1,1),
                  dt(YEAR,1,6),
                  dt(YEAR,4,25),
                  dt(YEAR,5,1),
                  dt(YEAR,6,2),
                  dt(YEAR,6,24),
                  dt(YEAR,8,15),
                  dt(YEAR,9,1),
                  dt(YEAR,12,8),
                  dt(YEAR,12,25),
                  dt(YEAR,12,26),
                  easter(YEAR)+timedelta(days=1),
                  easter(YEAR)]

arbitrary_holidays = [dt(YEAR,4,30),
                      dt(YEAR,5,3),
                      dt(YEAR,6,21),
                      dt(YEAR,6,22),
                      dt(YEAR,6,23),
                      dt(YEAR,7,19),
                      dt(YEAR,7,20),
                      dt(YEAR,7,21),
                      dt(YEAR,7,22),
                      dt(YEAR,7,23),
                      dt(YEAR,7,24),
                      dt(YEAR,9,6),
                      dt(YEAR,9,7),
                      dt(YEAR,9,8),
                      dt(YEAR,9,9),
                      dt(YEAR,9,10),
                      dt(YEAR,9,11),]

allholidays = fixed_holidays + arbitrary_holidays