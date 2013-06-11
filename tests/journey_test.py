import unittest
import datetime
import time
from oyster.journey import OysterJourney
from datetime import date


class OysterJourneyTest(unittest.TestCase):
    date = '31-May-2013'
    startTime = '17:03'
    endTime = '18:07'
    journey = 'Syon Lane [National Rail] to Deptford [National Rail]'
    cost = '3.60'

    def setUp(self):
        self.underTest = OysterJourney(self.date, self.startTime, self.endTime, self.journey, self.cost)

    def test_oyster_journey_journey(self):
        self.assertEquals(self.journey, self.underTest.description)

    def test_oyster_journey_date(self):
        self.assertTrue(isinstance(self.underTest.date, date), 'Date is of wrong type')
        self.assertEquals(self.underTest.date, datetime.datetime.strptime("31-May-2013", "%d-%b-%Y"))

    def test_oyster_journey_description(self):
        self.assertEquals(self.journey, self.underTest.description)

    def test_oyster_journey_cost(self):
        self.assertEquals(self.cost, self.underTest.cost)

    def test_oyster_journey_end_time(self):
        self.assertEquals(self.underTest.endTime, time.strptime("18:07", "%H:%M"))

    def test_oyster_journey_start_time(self):
        self.assertEquals(self.underTest.startTime, time.strptime("17:03", "%H:%M"))
