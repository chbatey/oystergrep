import logging


class JourneyCategoriser(object):
    # TODO: What does it mean if there are variables here?
    # work_journeys = []

    def __init__(self, work_location):
        self.work_journeys = []
        self.work_location = work_location

    def categorise(self, journeys):

        for journey in journeys:
            # TODO: Should handle incorrect type
            if journey.from_station == self.work_location or journey.to_station == self.work_location:
                logging.debug("Adding work journey %s", journey)
                self.work_journeys.append(journey)

    def get_work_journeys(self):
        # TODO: Should this be a defensive copy?
        return self.work_journeys