from objects import Program, Colour
from settings import MORNING_OPEN, MORNING_CLOSE, AFTERNON_OPEN, AFTERNOON_CLOSE, ANIMATIONS_OPEN, ANIMATIONS_SHIFT

morning = Program(MORNING_OPEN, MORNING_CLOSE, ANIMATIONS_OPEN)
afternoon = Program(AFTERNON_OPEN, AFTERNOON_CLOSE, ANIMATIONS_OPEN)

shift_begin = Program(MORNING_OPEN, (24,0), ANIMATIONS_SHIFT)
shift_end = Program((0,0), MORNING_OPEN, ANIMATIONS_SHIFT)
shift_day = Program((0,0), (24,0), ANIMATIONS_SHIFT)


col_monday = Colour(0, [afternoon])
col_work_day = Colour(1, [morning, afternoon])
col_shiftbegin = Colour(2, [shift_begin])
col_shiftday = Colour(3, [shift_day])
col_shiftend = Colour(4, [shift_end, morning])
col_shiftendholiday = Colour(5, [shift_end])