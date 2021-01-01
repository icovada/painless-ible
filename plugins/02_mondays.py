import plugin_collection 
from settings import MORNING, AFTERNOON, ANIMATIONS_OPEN, ANIMATIONS_SHIFT

class Mondays(plugin_collection.Plugin):
    """
    This plugin fills the week with standard weekday configuration
    """
    def __init__(self):
        super().__init__()
        self.priority = 2
        self.description = 'Mondays'

    def perform_operation(self, argument):
        for k, v in argument.items():
            if v.dt.isoweekday() == 1:
                v.morning = None

        return argument
