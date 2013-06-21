import unittest
import datetime
import time
from oyster.journey import OysterJourney
from datetime import date

#TODO: Change cost to something that isn't a float!
class OysterJourneyTest(unittest.TestCase):
    date = '31-May-2013'
    startTime = '17:03'
    endTime = '18:07'
    journey_description = 'Syon Lane [National Rail] to Deptford [National Rail]'
    cost = '3.60'
    from_station = "Syon Lane [National Rail]"
    to_station = "Deptford [National Rail]"

    def setUp(self):
        self.under_test = OysterJourney(self.date, self.startTime, self.endTime, self.journey_description, self.cost, self.from_station, self.to_station)

    def test_oyster_journey_journey(self):
        self.assertEquals(self.journey_description, self.under_test.description)

    def test_oyster_journey_date(self):
        self.assertTrue(isinstance(self.under_test.date, date), 'Date is of wrong type')
        self.assertEquals(datetime.datetime.strptime("31-May-2013", "%d-%b-%Y"), self.under_test.date)

    def test_oyster_journey_description(self):
        self.assertEquals(self.journey_description, self.under_test.description)

    def test_oyster_journey_cost(self):
        self.assertEquals(3.60, self.under_test.cost)

    def test_oyster_journey_end_time(self):
        self.assertEquals(time.strptime("18:07", "%H:%M"), self.under_test.end_time )

    def test_oyster_journey_start_time(self):
        self.assertEquals(time.strptime("17:03", "%H:%M"), self.under_test.start_time)

    def test_oyster_from_station(self):
        self.assertEquals(self.from_station, self.under_test.from_station)

    def test_oyster_to_station(self):
        self.assertEquals(self.to_station, self.under_test.to_station)


