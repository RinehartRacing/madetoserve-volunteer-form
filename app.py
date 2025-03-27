from flask import Flask
from flask import render_template
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

    # Render the calendar as HTML
    return f"""
    <html>
        <head>
            <title>Calendar</title>
        </head>
        <body>
            <h1>Calendar for {calendar.month_name[month]} {year}</h1>
            {cal}
        </body>
    </html>
    """
