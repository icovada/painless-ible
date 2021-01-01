from inspect import ArgInfo
import plugin_collection 
from settings import ANIMATIONS_OPEN

class Weekdays(plugin_collection.Plugin):
    """
    This plugin fills the week with standard weekday configuration
    """
    def __init__(self):
        super().__init__()
        self.priority = 1
        self.description = 'Weekdays'

    def perform_operation(self, argument):
        for k, v in argument.items():
            if not v.holiday:
                v.morning = "ANIMATIONS_OPEN"
                v.afternoon = "ANIMATIONS_OPEN"

        return argument