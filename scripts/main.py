import calendar
from datetime import date
from visitors import *

conference = {
    date(2025, 3, 5): "Project deadline",
    date(2025, 3, 6): "Project deadline",
    date(2025, 3, 7): "Project deadline",
    date(2025, 3, 8): "Project deadline",
    date(2025, 3, 9): "Project deadline",
    date(2025, 3, 10): "Project deadline",
    date(2025, 3, 12): "Team meeting",
    date(2025, 3, 25): "Conference",
    date(2025, 3, 26): "Conference",
    date(2025, 3, 27): "Conference",
    date(2025, 3, 28): ["Conference", "Dinner"],
}


CEP = ListCandidates()


class MonthlySchedule(calendar.HTMLCalendar):

    def __init__(self, year: int, month: int, events: dict):

        super().__init__(firstweekday=0)
        self.events = events
        self._year = year
        self._month = month

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    def addEvent(self, datetime, title):
        self.events[datetime] = title

    def formatday(self, day, weekday):

        """
        Return a day as a table cell.
        """

        if day == 0:
            # day outside month
            return '<td class="%s">&nbsp;</td>' % self.cssclass_noday
        else:
            d = date(self.year, self.month, day)
            if d in self.events:
                if len(self.events[d]) > 1:
                    # Add a CSS class and tooltip text
                    return f'<td class="event-day"><strong>{day}</strong><br><small>{self.events[d]}</small></td>'
                else:
                    # Add a CSS class and tooltip text
                    return f'<td class="event-day"><strong>{day}</strong><br><small>{self.events[d]}</small></td>'
            else:
                return '<td class="%s">%d</td>' % (self.cssclasses[weekday], day)

    def displayMonth(self):

        # Override to pass year & month to formatday
        output = '<table border="1" cellpadding="4" cellspacing="0">\n'
        output += f"{self.formatmonthname(self.year, self.month, withyear=True)}\n"
        output += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            output += "<tr>"
            for day, weekday in week:
                output += self.formatday(day, weekday)
            output += "</tr>\n"
        output += "</table>"

        # Wrap in a basic HTML page with some style
        page = f"""<!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <title>Calendar {'March'}/{2025}</title>
        <style>
          table {{ border-collapse: collapse; }}
          th, td {{ width: 80px; height: 60px; text-align: center; vertical-align: top; }}.event-day {{ background-color: #ffefc2; }}
        </style>
        </head>
        <body>
        {output}
        </body>
        </html>
        """

        with open(f"calendar_{self.year}_{self.month}.html", "w", encoding="utf-8") as f:
            f.write(page)

        return output


cal = MonthlySchedule(year=2025, month=3, events=conference)
html = cal.displayMonth()


# #
# # text_calendar = calendar.TextCalendar()
# # text_calendar.pryear(2025)
