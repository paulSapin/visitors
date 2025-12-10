import calendar
from datetime import date
from visitors import *

events = {
    date(2025, 3, 5): "Project deadline",
    date(2025, 3, 12): "Team meeting",
    date(2025, 3, 25): "Conference",
}


C = Calendar()


class EventHTMLCalendar(calendar.HTMLCalendar):

    def __init__(self, events):
        super().__init__(firstweekday=0)
        self.events = events

    def formatday(self, day, weekday, year, month):
        if day == 0:
            return "<td></td>"  # Empty cell

        d = date(year, month, day)
        if d in self.events:
            # Add a CSS class and tooltip text
            return f'<td class="event-day"><strong>{day}</strong><br><small>{self.events[d]}</small></td>'
        else:
            return f"<td>{day}</td>"

    def formatmonth(self, year, month, with_year=True):
        # Override to pass year & month to formatday
        cal = '<table border="1" cellpadding="4" cellspacing="0">\n'
        cal += f"{self.formatmonthname(year, month, withyear=with_year)}\n"
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(year, month):
            cal += "<tr>"
            for day, weekday in week:
                cal += self.formatday(day, weekday, year, month)
            cal += "</tr>\n"
        cal += "</table>"
        return cal


year = 2025
month = 3
cal = EventHTMLCalendar(events)
html = cal.formatmonth(year, month)

# Wrap in a basic HTML page with some style
page = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Calendar {month}/{year}</title>
<style>
  table {{ border-collapse: collapse; }}
  th, td {{ width: 80px; height: 60px; text-align: center; vertical-align: top; }}.event-day {{ background-color: #ffefc2; }}
</style>
</head>
<body>
{html}
</body>
</html>
"""

with open("calendar.html", "w", encoding="utf-8") as f:
    f.write(page)

print("Open calendar.html in your browser.")

text_calendar = calendar.TextCalendar()
text_calendar.pryear(2025)
