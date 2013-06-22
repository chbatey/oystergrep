import sys
import getopt

from oyster.journey_analyser import JourneyAnalyser
from oyster.journey_categoriser import JourneyCategoriser
from oyster.journey_parser import JourneyParser

if not len(sys.argv) > 1:
    print "usgae: monthlysummary.py -i <inputfile> -w <worklocation> -m <month>"
    sys.exit(2)

try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:w:m:")
except getopt.GetoptError:
    print "error usgae: monthlysummary.py -i <inputfile> -w <worklocation> -m <month>"
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print "monthlysummary.py -i <inputfile> -w <worklocation> -m <month>"
        sys.exit()
    elif opt == '-i':
        file_location = arg
    elif opt == '-w':
        work_location = arg
    elif opt == '-m':
        month = int(arg)

parser = JourneyParser()
journeys = parser.parse(file_location).journeys

categoriser = JourneyCategoriser(work_location)
categoriser.categorise(journeys)
work_journeys = categoriser.get_work_journeys()


analyser = JourneyAnalyser()
analysis = analyser.analyse_journeys(work_journeys)

month = analysis.get_month_breakdown(month)

weeks = month.get_week_breakdown()

for week in weeks:
    print week.get_summary() + "\n"