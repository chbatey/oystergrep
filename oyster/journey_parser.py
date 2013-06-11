import csv
import logging
from journey import OysterJourney


class JourneyParser(object):
    def parse(self, fileLocation):
        journeys = []
        with open(fileLocation, 'rb') as csvfile:
            filereader = csv.reader(csvfile)
            for row in filereader:
                if len(row) == 8:
                    if row[0] != 'Date':
                        if not (row[3].startswith("Auto top-up")):
                            journey = OysterJourney(row[0], row[1], row[2], row[3], row[4])
                            journeys.append(journey)
                else:
                    logging.info('Line does not contain 8 rows ignoring: %s' % row)

        return JourneyParseResults(journeys)

# Returning an object rather than the list directly so can add
# top ups etc to the result
class JourneyParseResults(object):
    def __init__(self, journeys):
        self.journeys = journeys
