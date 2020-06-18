#!/usr/bin/env python
import sys

# The icalendar library is used for parsing through ics files.
import icalendar
from icalendar import Calendar, Event
from datetime import datetime, timedelta, date
from operator import itemgetter

def convert_calendar(calendar, date):
    # Open file with the ics calendar in it and then read it into an icalendar object.
    f = open(calendar, 'rb')
    process_cal = Calendar.from_ical(f.read())
    f.close()

    # cal_events is a list of every event in the calendar.
    cal_events = [e for e in process_cal.walk('vevent')]
    first_event_date = get_first_event_date(cal_events)

    # The offset is how many days we are moving the dates of the calendar.
    offset = date - first_event_date
    # Every date in every event is moved by the offset.
    for e in cal_events:
        e['DTSTART'].dt = e['DTSTART'].dt + offset
        e['DTEND'].dt = e['DTEND'].dt + offset
    # Call function to change weekly dates.
    change_weekly(cal_events)
    # output to file.
    f = open('output.ics', 'wb')
    f.write(process_cal.to_ical())
    f.close()

# Converts the date of the first calendar event into datetime.date object for easy comparison if it is not already.
def get_first_event_date(cal_events):
    # Get the first event in the list, take note however, this is not necessarily the first chronological date.
    first_event = cal_events[0]
    first_event_date = 0
    for e in cal_events:
        if isinstance(first_event['DTSTART'].dt, datetime):
            first_event_date = datetime.date(first_event['DTSTART'].dt)
            #first_event['DTEND'].dt = datetime.date(first_event['DTEND'].dt)
        else:
            first_event_date = first_event['DTSTART'].dt
        type_compare_date = e['DTSTART'].dt
        if isinstance(type_compare_date, datetime):
            compare_date = datetime.date(type_compare_date)
        else:
            compare_date = type_compare_date
        if compare_date<first_event_date:
            first_event = e
    return first_event_date

# This method will change the weekly repeats in weekly events.
def change_weekly(cal_events):
    # Cypher of dates for repeating weekly RRULE.
    dates = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA','SU']
    for e in cal_events:
        # Any weekly events have their repeat dates change. Does this by getting the new day of the week the event starts on 
        if str(e['SUMMARY']) == "weekly":
            e['RRULE']['BYDAY'] = dates[e['DTSTART'].dt.weekday()]
            

if __name__ == '__main__':
    # Calendar file name is first command line arg, then year, month and day. The date and the calendar file name is then passed into the convert_calendar method.
    cal = sys.argv[1]
    year = int(sys.argv[2])
    month = int(sys.argv[3])
    day = int(sys.argv[4])
    dt = date(year, month, day)
    convert_calendar(cal, dt)