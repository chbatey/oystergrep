import csv
import logging
from journey import OysterJourney

DESCRIPTION_SPLITTER = " to "
AUTO_TOP_UP = "Auto top-up"
FIRST_COLUMN = 'Date'
COLS_PER_ROW = 8


class JourneyParser(object):
    def parse(self, fileLocation):
        journeys = []
        with open(fileLocation, 'rb') as csv_file:
            file_reader = csv.reader(csv_file)
            for row in file_reader:
                if len(row) == COLS_PER_ROW and row[0] != FIRST_COLUMN:
                    if not (row[3].startswith(AUTO_TOP_UP)):
                        to_and_from = row[3].split(DESCRIPTION_SPLITTER)
                        logging.debug(to_and_from)
                        journey = OysterJourney(row[0], row[1], row[2], row[3], row[4], to_and_from[0], to_and_from[1])
                        journeys.append(journey)
                else:
                    logging.info('Line does not contain 8 rows ignoring: %s' % row)

        return JourneyParseResults(journeys)


# Returning an object rather than the list directly so can add
# top ups etc to the result
class JourneyParseResults(object):
    def __init__(self, journeys):
        self.journeys = journeys
