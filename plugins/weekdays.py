import plugin_collection 
from settings import MORNING, AFTERNON

class Weekdays(plugin_collection.Plugin):
    """
    This plugin fills the week with standard weekday configuration
    """
    def __init__(self):
        super().__init__()
        self.priority = 0
        self.description = 'Weekdays'

    def perform_operation(self, argument):
        for k, v in argument.items():
            if not v.holiday:
                v.schedule = [MORNING, AFTERNON]
