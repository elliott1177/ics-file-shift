# The icalendar library is used for parsing through ics files.
import icalendar
from icalendar import Calendar, Event

def convert_calendar(calendar, date):
    f = open(calendar, 'rb')
    process_cal = Calendar.from_ical(f.read())
    for event in process_cal.walk('vevent'):
        print(event['DTSTART'])
        print(event['DTSTART'].dt)
