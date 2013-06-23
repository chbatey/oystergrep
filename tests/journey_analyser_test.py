import datetime
from unittest import TestCase
from oyster.journey import OysterJourney
from oyster.journey_analyser import JourneyAnalyser, WeekBreakdown


class JourneyAnalyserTest(TestCase):
    default_cost = "1.00"
    default_start_time = "07:00"
    default_end_time = "17:00"
    default_date = "29-May-2013"
    default_description = "Somewhere to somewhere else"
    default_from = "Somewhere"
    default_to = "somewhere else"

    def setUp(self):
        self.under_test = JourneyAnalyser()

    def test_total_cost_for_no_journeys(self):
        #given
        journeys = []
        #when
        analysis = self.under_test.analyse_journeys(journeys)
        #then
        self.assertAlmostEqual(0.0, analysis.get_total_cost())

    def test_total_cost_for_single_journey(self):
        #given
        cost = 10.0
        journeys = [self.__journey_with_cost(cost)]
        #when
        analysis = self.under_test.analyse_journeys(journeys)
        #then
        self.assertAlmostEqual(cost, analysis.get_total_cost())

    def test_total_cost_for_many_journeys(self):
        #given
        expected_cost = 29.25
        journeys = [self.__journey_with_cost(10.0),
                    self.__journey_with_cost(15.0),
                    self.__journey_with_cost(4.25)]

        #when
        analysis = self.under_test.analyse_journeys(journeys)
        #then
        self.assertAlmostEqual(expected_cost, analysis.get_total_cost())

    def test_monthly_break_down_total_journeys(self):
        #given
        journeys = [self.__journey_with_date("15-April-2013"),
                    self.__journey_with_date("15-May-2013"),
                    self.__journey_with_date("16-May-2013")]
        #when
        analysis = self.under_test.analyse_journeys(journeys)
        may_break_down = analysis.get_month_breakdown(5)
        #then
        self.assertAlmostEqual(2, len(may_break_down.get_journeys()))

    def test_monthly_break_down_total_cost(self):
        #given
        journeys = [self.__journey_with_date("15-April-2013"),
                    self.__journey_with_date("15-May-2013"),
                    self.__journey_with_date("16-May-2013")]
        #when
        analysis = self.under_test.analyse_journeys(journeys)
        may_break_down = analysis.get_month_breakdown(5)
        #then
        self.assertAlmostEqual(2.0, may_break_down.get_total_cost())

    def test_weekly_break_down_week_splitting(self):
        #given
        journeys = []
        #when
        analysis = self.under_test.analyse_journeys(journeys)
        may_break_down = analysis.get_month_breakdown(5)
        week_break_down = may_break_down.get_week_breakdown()
        #then
        self.assertEqual(5, len(week_break_down))
        print(week_break_down[0].get_start_date())
        self.assertEqual(datetime.date(2013, 5, 1), week_break_down[0].get_start_date())
        self.assertEqual(datetime.date(2013, 5, 5), week_break_down[0].get_end_date())

        self.assertEqual(datetime.date(2013, 5, 6), week_break_down[1].get_start_date())
        self.assertEqual(datetime.date(2013, 5, 12), week_break_down[1].get_end_date())

        self.assertEqual(datetime.date(2013, 5, 13), week_break_down[2].get_start_date())
        self.assertEqual(datetime.date(2013, 5, 19), week_break_down[2].get_end_date())

        self.assertEqual(datetime.date(2013, 5, 20), week_break_down[3].get_start_date())
        self.assertEqual(datetime.date(2013, 5, 26), week_break_down[3].get_end_date())

        self.assertEqual(datetime.date(2013, 5, 27), week_break_down[4].get_start_date())
        self.assertEqual(datetime.date(2013, 5, 31), week_break_down[4].get_end_date())

    def test_weekly_break_down_week_allocating_journeys(self):
        #given
        week1_1 = self.__journey_with_date("01-May-2013")
        week1_2 = self.__journey_with_date("05-May-2013")
        week3_1 = self.__journey_with_date("13-May-2013")
        week4_1 = self.__journey_with_date("26-May-2013")
        journeys = [self.__journey_with_date("29-April-2013"),
                    week1_1,
                    week1_2,
                    week3_1,
                    week4_1,
                    self.__journey_with_date("02-June-2013")]
        #when
        analysis = self.under_test.analyse_journeys(journeys)
        may_break_down = analysis.get_month_breakdown(5)
        week_break_down = may_break_down.get_week_breakdown()
        #then
        self.assertEqual(2, len(week_break_down[0].get_journeys()))
        self.assertEqual(week1_1, week_break_down[0].get_journeys()[0])
        self.assertEqual(week1_2, week_break_down[0].get_journeys()[1])

        self.assertEqual(0, len(week_break_down[1].get_journeys()))

        self.assertEqual(1, len(week_break_down[2].get_journeys()))
        self.assertEqual(week3_1, week_break_down[2].get_journeys()[0])

        self.assertEqual(1, len(week_break_down[3].get_journeys()))
        self.assertEqual(week4_1, week_break_down[3].get_journeys()[0])

        self.assertEqual(0, len(week_break_down[4].get_journeys()))

    def test_weekly_break_down_total_cost(self):
        #given
        week1_1 = self.__journey_with_date("01-May-2013")
        week1_2 = self.__journey_with_date("05-May-2013")
        week3_1 = self.__journey_with_date("13-May-2013")
        week4_1 = self.__journey_with_date("26-May-2013")
        journeys = [self.__journey_with_date("29-April-2013"),
                    week1_1,
                    week1_2,
                    week3_1,
                    week4_1,
                    self.__journey_with_date("02-June-2013")]
        week_break_down = WeekBreakdown(datetime.datetime.strptime("01-May-2013", "%d-%B-%Y").date(),
                                        datetime.datetime.strptime("05-May-2013", "%d-%B-%Y").date())
        #when
        week_break_down._add_journeys(journeys)
        week_journeys = week_break_down.get_journeys()
        #then
        self.assertEqual(2, len(week_journeys))
        self.assertEqual(week1_1, week_journeys[0])
        self.assertEqual(week1_2, week_journeys[1])
        self.assertAlmostEqual(2.0, week_break_down.get_total_cost())

    def __journey_with_cost(self, cost):
        return OysterJourney(self.default_date, self.default_start_time,
                             self.default_end_time, self.default_description,
                             cost, self.default_from, self.default_to)

    def __journey_with_date(self, date):
        return OysterJourney(date, self.default_start_time,
                             self.default_end_time, self.default_description,
                             self.default_cost, self.default_from, self.default_to)

