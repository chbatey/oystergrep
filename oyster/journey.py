import datetime
import time


class OysterJourney:
    def __init__(self, date, start_time, end_time, journey, cost, from_station, to_station):
        self.data = []
        self.date = datetime.datetime.strptime(date, "%d-%b-%Y")
        self.start_time = time.strptime(start_time, "%H:%M")
        self.end_time = time.strptime(end_time, "%H:%M")
        self.description = journey
        self.cost = cost
        self.from_station = from_station
        self.to_station = to_station

