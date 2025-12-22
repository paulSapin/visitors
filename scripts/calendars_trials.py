import datetime as dt
import calendar
import matplotlib.pyplot as plt
from collections import defaultdict


# ---- 1. Define events ----
# Each event: title, start_date, end_date (inclusive)
events = [
    {
        "title": "Yuhui Song (PhD)",
        "start": dt.date(year=2025, month=1, day=1),
        "end": dt.date(year=2025, month=10, day=31),
        "color": "blue",
    },
    {
        "title": "Jingyu Gao (PhD)",
        "start": dt.date(year=2025, month=6, day=1),
        "end": dt.date(year=2025, month=10, day=15),
        "color": "green",
    },
    {
        "title": "Shuoyu Zhang (PhD)",
        "start": dt.date(year=2025, month=1, day=1),
        "end": dt.date(year=2027, month=10, day=31),
        "color": "red",
    }
]

def displaySchedule(year: int):


    # ---- 2. Utility to iterate dates ----
    def daterange(start_date, end_date):
        """Yield each date from start to end inclusive."""
        cur = start_date
        while cur <= end_date:
            yield cur
            cur += dt.timedelta(days=1)

    # ---- 3. Build day -> list of events mapping ----
    # key: date, value: list of events that cover this date
    events_by_day = defaultdict(list)

    for ev in events:
        # Clip events to the selected year only
        start = max(ev["start"], dt.date(year, 1, 1))
        end = min(ev["end"], dt.date(year, 12, 31))
        if start > end:
            continue  # event doesn't intersect this year

        for d in daterange(start, end):
            events_by_day[d].append(ev)

    # ---- 4. Assign lanes per day to handle overlaps ----
    # For each day, overlapping events get different vertical lanes.
    lanes_by_day = {}

    for day, evs in events_by_day.items():
        # Simple lane assignment: just index them
        # (for more advanced layouts you can reuse lanes across consecutive days)
        lanes_by_day[day] = {id(ev): lane for lane, ev in enumerate(evs)}

    # ---- 5. Plot the year using Matplotlib ----
    fig, ax = plt.subplots(figsize=(16, 9))

    # Set up grid limits:
    # x-axis: days 1..31
    # y-axis: months 1..12
    ax.set_xlim(0.5, 31.5)
    ax.set_ylim(12, 0)  # invert y so Jan at top (month 1)

    ax.set_xticks(range(1, 32))
    ax.set_yticks(range(1, 13))
    ax.set_yticklabels([calendar.month_abbr[m] for m in range(1, 13)])

    ax.set_xlabel("Day of Month")
    ax.set_title(f"Year {year} Calendar with Multi-Day Events")

    # Draw light grid for visual structure
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.5)

    # ---- 6. Draw each event as daily blocks ----
    # Parameters to control visual appearance
    day_width = 0.95               # width of a day cell
    lane_height = 0.2             # height of one event lane inside a month row
    lane_padding = 0.05           # small vertical gap between lanes

    for day, evs in events_by_day.items():
        month = day.month
        day_of_month = day.day

        # sort events for stable coloring/text
        # (optional, but keeps same order)
        evs_sorted = list(evs)

        for ev in evs_sorted:
            lane = lanes_by_day[day][id(ev)]

            # Base y for this month
            # Row center is at "month"
            # We'll stack lanes downward from the center.
            y_base = month
            # Shift event rectangles vertically depending on lane
            # Example: lane 0: centered at month - 0.25, lane 1: month - 0.25 - 0.25, etc.
            y_center = y_base - 0.1 - lane * (lane_height + lane_padding)

            # Rectangle bottom
            y_bottom = y_center - lane_height / 2
            # Rectangle left
            x_left = day_of_month - day_width / 2

            rect = plt.Rectangle(
                (x_left, y_bottom),
                day_width,
                lane_height,
                color=ev.get("color", "#1f77b4"),
                alpha=0.8,
            )
            ax.add_patch(rect)

            # Optionally write a short label on first day of an event segment
            if day == max(ev["start"], dt.date(year, 1, 1)):
                ax.text(
                    day_of_month,
                    y_center,
                    ev["title"],
                    ha="left",
                    va="center",
                    fontsize=6,
                    color="black",
                    clip_on=True,
                    bbox=dict(facecolor='white', edgecolor='none', pad=0.5)
                )

    # Improve layout
    plt.tight_layout()
    plt.show()

displaySchedule(year=2027)