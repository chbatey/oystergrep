import datetime
import time

class OysterJourney:
    def __init__(self, date, startTime, endTime, journey, cost):
        self.data = []
        self.date = datetime.datetime.strptime(date, "%d-%b-%Y")
        self.startTime = time.strptime(startTime, "%H:%M")
        self.endTime = time.strptime(endTime, "%H:%M")
        self.description = journey
        self.cost = cost

    def __str__(self):
        return 'to string here'

    def someOtherMethod(self):
        print "hello from some other method"
