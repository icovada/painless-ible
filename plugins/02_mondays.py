import plugin_collection 

class Mondays(plugin_collection.Plugin):
    """
    This plugin applies Monday morning closre on all Mondays
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
