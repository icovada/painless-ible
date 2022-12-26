import plugin_collection
from settings import ANIMATIONS_OPEN, ANIMATIONS_SHIFT, FIRST_SHIFT_BEGIN, SHIFT_DURATION, SHIFT_ROTATION_DAYS


class Shifts(plugin_collection.Plugin):
    """
    This plugin applies Shift animations on Shift days
    """

    def __init__(self):
        super().__init__()
        self.priority = 3
        self.description = 'Shifts'

    def perform_operation(self, argument):
        found_first = False
        shift_day = 0
        for k, v in argument.items():
            if not found_first:
                if v.dt == FIRST_SHIFT_BEGIN:
                    found_first = True
                else:
                    continue

            if shift_day == 0:
                v.morning = "ANIMATIONS_SHIFT"
                v.lunch = "ANIMATIONS_SHIFT"
                v.afternoon = "ANIMATIONS_SHIFT"
                v.night_end = "ANIMATIONS_SHIFT"
            elif shift_day > 0 and shift_day < SHIFT_DURATION:
                v.night_begin = "ANIMATIONS_SHIFT"
                v.morning = "ANIMATIONS_SHIFT"
                v.lunch = "ANIMATIONS_SHIFT"
                v.afternoon = "ANIMATIONS_SHIFT"
                v.night_end = "ANIMATIONS_SHIFT"
            elif shift_day == SHIFT_DURATION:
                v.night_begin = "ANIMATIONS_SHIFT"

                v.afternoon = None
                if v.holiday:
                    v.morning = None
                else:
                    v.morning = "ANIMATIONS_OPEN"

            if shift_day == SHIFT_ROTATION_DAYS-1:
                shift_day = 0
            else:
                shift_day = shift_day + 1

        return argument
