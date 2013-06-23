import logging
import calendar


class JourneyAnalyser:
    def analyse_journeys(self, journeys):
        total_cost = 0
        journeys_by_month = {}

        for journey in journeys:
            total_cost += journey.cost
            month = journey.date.month
            logging.debug("Month %s" % month)
            if month not in journeys_by_month:
                journeys_by_month[month] = []

            journeys_by_month[month].append(journey)

        return JourneyAnalysis(total_cost, journeys_by_month)


class JourneyAnalysis:
    def __init__(self, total_cost, journeys_by_month):
        self.total_cost = total_cost
        self.journeys_by_month = journeys_by_month

    def get_total_cost(self):
        return self.total_cost

    def get_month_breakdown(self, month):
        if month in self.journeys_by_month:
            return MonthBreakDown(self.journeys_by_month[month], month)
        else:
            return MonthBreakDown([], month)


class MonthBreakDown:
    def __init__(self, journeys, month):
        self._journeys = journeys
        self._month = month
        pass

    def get_total_cost(self):
        total = 0.0
        for journey in self._journeys:
            total += journey.cost
        return total

    def get_journeys(self):
        return self._journeys

    def get_week_breakdown(self):
        weeks = self.get_weeks(2013, self._month)
        for week in weeks:
            week._add_journeys(self._journeys)

        return weeks

    def get_weeks(self, year, month):
        cal = calendar.Calendar()
        iterator = cal.itermonthdates(year, month)
        day_of_week = 0
        weeks = []
        current_week = []
        for date in iterator:
            day_of_week += 1
            if date.month == month:
                current_week.append(date)
            if day_of_week == 7:
                weeks.append(WeekBreakdown(current_week[0], current_week[-1]))
                day_of_week = 0
                current_week = []

        return weeks


class WeekBreakdown:
    def __init__(self, start_date, end_date):
        self._end_date = end_date
        self._start_date = start_date
        self._journeys = []

    def get_start_date(self):
        return self._start_date

    def get_end_date(self):
        return self._end_date

    def _add_journeys(self, journeys):
        for journey in journeys:
            if self._start_date <= journey.date.date() <= self._end_date:
                self._journeys.append(journey)

    def get_journeys(self):
        return self._journeys

    def get_summary(self):
        to_return = "Week: " + str(self._start_date) + " to " + str(self._end_date) + " " + str(self.get_total_cost()) + "\n"
        for journey in self._journeys:
            to_return += str(journey.date) + " " + str(journey.cost) + " " + journey.description + "\n"

        return to_return

    def get_total_cost(self):
        total = 0.0
        for journey in self._journeys:
            total += journey.cost

        return total
