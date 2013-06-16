import unittest
import datetime
import time
from oyster.journey_parser import JourneyParser


class JourneyParserTest(unittest.TestCase):
    def setUp(self):
        self.underTest = JourneyParser()

    def test_parse_empty_file(self):
        fileLocation = './tests/testfiles/emptyfile.csv'
        journeys = self.underTest.parse(fileLocation).journeys
        self.assertEquals(0, len(journeys))

    def test_parse_just_headers(self):
        fileLocation = './tests/testfiles/justheaders.csv'
        journeys = self.underTest.parse(fileLocation).journeys
        self.assertEquals(0, len(journeys))

    def test_parse_single_row(self):
        fileLocation = './tests/testfiles/oneentry.csv'
        journeys = self.underTest.parse(fileLocation).journeys
        self.assertEquals(1, len(journeys))
        single_journey = journeys[0]
        self.__assert_journey(single_journey,
                              '31-May-2013',
                              "17:03",
                              "18:07",
                              "Syon Lane [National Rail] to Deptford [National Rail]",
                              "3.60",
                              "Syon Lane [National Rail]",
                              "Deptford [National Rail]")

    def test_parse_single_row_ignore_empty_lines(self):
        fileLocation = './tests/testfiles/oneentryblanklineattop.csv'
        journeys = self.underTest.parse(fileLocation).journeys
        self.assertEquals(1, len(journeys))
        single_journey = journeys[0]
        self.__assert_journey(single_journey,
                              '31-May-2013',
                              "17:03",
                              "18:07",
                              "Syon Lane [National Rail] to Deptford [National Rail]",
                              "3.60",
                              "Syon Lane [National Rail]",
                              "Deptford [National Rail]")

    def test_parse_multiple_rows(self):
        fileLocation = './tests/testfiles/manyentries.csv'
        journeys = self.underTest.parse(fileLocation).journeys
        self.assertEquals(7, len(journeys))

#       30-May-2013,07:21,08:26,"Deptford [National Rail] to Syon Lane [National Rail]",3.60,,7.05,""

        self.__assert_journey(journeys[1],
                          '30-May-2013',
                          "07:21",
                          "08:26",
                          "Deptford [National Rail] to Syon Lane [National Rail]",
                          "3.60",
                          "Deptford [National Rail]",
                          "Syon Lane [National Rail]")
#       29-May-2013,17:02,18:02,"Syon Lane [National Rail] to Old Street",5.10,,12.55,""
        self.__assert_journey(journeys[2],
                      '29-May-2013',
                      "17:02",
                      "18:02",
                      "Syon Lane [National Rail] to Old Street",
                      "5.10",
                      "Syon Lane [National Rail]",
                      "Old Street")

    def test_parse_ignored_topups(self):
        fileLocation = './tests/testfiles/autotopup.csv'
        journeys = self.underTest.parse(fileLocation).journeys
        self.assertEquals(1, len(journeys))

    def test_parse_capped_journey(self):
        fileLocation = './tests/testfiles/cappedjourney.csv'
        journeys = self.underTest.parse(fileLocation).journeys
        self.assertEquals(1, len(journeys))
        #9-May-2013,20:11,20:45,"Barbican to Cutty Sark DLR",1.90,,10.65,"The fare for this journey was capped as you reached the daily charging limit for the zones used"
        self.__assert_journey(journeys[0],
              '9-May-2013',
              "20:11",
              "20:45",
              "Barbican to Cutty Sark DLR",
              "1.90",
              "Barbican",
              "Cutty Sark DLR")

    # TODO handle malformed files

    def __assert_journey(self, single_journey, date, start_time, end_time, journey, cost, from_station, to_station):
        self.assertEquals(datetime.datetime.strptime(date, "%d-%b-%Y"), single_journey.date)
        self.assertEquals(time.strptime(start_time, "%H:%M"), single_journey.start_time)
        self.assertEquals(time.strptime(end_time, "%H:%M"), single_journey.end_time)
        self.assertEquals(journey, single_journey.description)
        self.assertEquals(cost, single_journey.cost)
        self.assertEquals(from_station, single_journey.from_station)
        self.assertEquals(to_station, single_journey.to_station)

