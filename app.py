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

    # Render the calendar as HTML with inline CSS
    return f"""
    <html>
        <head>
            <title>Calendar</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    color: #333;
                    text-align: center;
                    margin: 0;
                    padding: 0;
                }}
                h1 {{
                    color: #4CAF50;
                }}
                table {{
                    margin: 20px auto;
                    border-collapse: collapse;
                    width: 80%;
                    max-width: 800px;
                    font-size: 1.2em;
                }}
                th {{
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px;
                }}
                td {{
                    border: 1px solid #ddd;
                    padding: 10px;
                    text-align: center;
                }}
                td:hover {{
                    background-color: #f1f1f1;
                }}
                tr:nth-child(even) {{
                    background-color: #f9f9f9;
                }}
            </style>
        </head>
        <body>
            <h1>Calendar for {calendar.month_name[month]} {year}</h1>
            {cal}
        </body>
    </html>
    """
