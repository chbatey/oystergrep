from unittest import TestCase
from oyster.journey import OysterJourney
from oyster.journey_categoriser import JourneyCategoriser

WORK_LOCATION = "Syon Lane [National Rail]"


class JourneyCategoriserTest(TestCase):

    default_cost = "3.20"
    default_start_time = "07:00"
    default_end_time = "17:00"
    default_date = "29-May-2013"
    default_description = "Somewhere to somewhere else"
    default_from = "Somewhere"
    default_to = "somewhere else"

    def setUp(self):
        self.under_test = JourneyCategoriser(WORK_LOCATION)

    def test_no_work_journeys(self):
        #given
        journeys = [self.__journey()]
        #when
        self.under_test.categorise(journeys)
        work_journeys = self.under_test.get_work_journeys()
        #then
        self.assertEqual(0, len(work_journeys))

    def test_one_work_journey_from_work(self):
        #given
        work_journey = self.__journey_from_to(WORK_LOCATION, "Anywhere")
        journeys = [work_journey]
        #when
        self.under_test.categorise(journeys)
        work_journeys = self.under_test.get_work_journeys()
        #then
        self.assertEqual(1, len(work_journeys))

    def test_one_work_journey_to_work(self):
        #given
        work_journey = self.__journey_from_to("Anywhere", WORK_LOCATION)
        journeys = [work_journey]
        #then
        self.under_test.categorise(journeys)
        work_journeys = self.under_test.get_work_journeys()
        #then
        self.assertEqual(1, len(work_journeys))

    def __journey_from_to(self, from_station, to_station):
        journey = self.__journey()
        journey.from_station = from_station
        journey.to_station = to_station
        return journey

    def __journey(self):
        return OysterJourney(self.default_date, self.default_start_time,
                             self.default_end_time, self.default_description,
                             self.default_cost, self.default_from, self.default_to)
