from datetime import datetime as dt

YEAR = 2021
SHIFT_DURATION = 7
FIRST_SHIFT_BEGIN = dt(2021, 1, 16)
SHIFT_ROTATION_DAYS = 28

TIME_NIGHT_BEGIN = [(0,0), (8,30)]
TIME_MORNING = [TIME_NIGHT_BEGIN[1], (13,0)]
TIME_LUNCH = [TIME_MORNING[1], (15,0)]
TIME_AFTERNOON = [TIME_LUNCH[1], (19,30)]
TIME_NIGHT_END = [TIME_AFTERNOON[1], (24,0)]


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

ANIMATION_CLOSED = "CHIUSOoradata"