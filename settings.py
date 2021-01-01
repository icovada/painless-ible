from datetime import datetime as dt

YEAR = 2021
SHIFT_DURATION = 7
FIRST_SHIFT_BEGIN = dt(2021, 1, 16)
SHIFT_ROTATION_DAYS = 28

NIGHT_BEGIN = [(0, 0), (8, 30)]
MORNING = [(8, 30), (13, 0)]
LUNCH = [(13, 0), (15, 0)]
AFTERNON = [(15, 0), (19, 30)]
NIGHT_END = [(19, 30), (24, 0)]

WORKING_DAY = [MORNING, AFTERNON]
MONDAY = [AFTERNON]

SHIFT_BEGIN_DAY = [MORNING, LUNCH, AFTERNON, NIGHT_END]
SHIFT_DAY = [NIGHT_BEGIN, MORNING, LUNCH, AFTERNON, NIGHT_END]
SHIFT_END = [NIGHT_BEGIN]

HOLIDAY = []

ANIMATIONS_SHIFT = [
    "APERTOoradata",
    "AS-02",
    "AS-03",
    "Caduceo",
    "GT-02",
    "GT-12",
    "Turno",
    "GT-23"
]
ANIMATIONS_OPEN = [
    "APERTOoradata",
    "AS-02",
    "AS-03",
    "Caduceo",
    "GT-02",
    "GT-12",
    "GT-23"
]
