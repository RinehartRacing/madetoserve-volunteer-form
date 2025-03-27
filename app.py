from flask import Flask, render_template
import calendar
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def calendar_view():
    # Get current year and month
    now = datetime.now()
    year = now.year
    month = now.month

    # Generate the calendar for the current month
    cal = calendar.HTMLCalendar().formatmonth(year, month)

    # Pass the calendar, month, and year to the template
    return render_template('index.html', calendar=cal, month=calendar.month_name[month], year=year)
