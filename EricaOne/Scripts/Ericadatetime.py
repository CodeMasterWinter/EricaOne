import time
import datetime


class DateTime:

    def __init__(self):
        self.now = datetime.datetime.now()

    def time(self, nonFormat=False):

        if nonFormat:
            return self.now.strftime("%H%M")
        else:
            return self.now.strftime("%H:%M")

    def hour(self):
        return self.now.strftime("%H")

    def minute(self):
        return self.now.strftime("%M")

    def month(self):
        return self.now.strftime("%B")