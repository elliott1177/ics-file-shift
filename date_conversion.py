#!/usr/bin/env python
import sys

# The icalendar library is used for parsing through ics files.
import tempfile, os
import icalendar
from icalendar import Calendar, Event
from datetime import datetime, timedelta, date
from operator import itemgetter

def convert_calendar(calendar, date):
    f = open(calendar, 'rb')
    process_cal = Calendar.from_ical(f.read())
    f.close()
    #for event in process_cal.walk('vevent'):
     #   print(event['DTSTART'].dt)
      #  print((event['DTSTART'].dt+timedelta(10)))
    cal_events = [e for e in process_cal.walk('vevent')]
    first_event = cal_events[0]
    first_event_date = 0
    isdate = False
    for e in cal_events:
        if isinstance(first_event['DTSTART'].dt, datetime):
            isdate = True
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
    # Remember to include negative vals.
    offset = date - first_event_date
    for e in cal_events:
        e['DTSTART'].dt = e['DTSTART'].dt + offset
        e['DTEND'].dt = e['DTEND'].dt + offset
    f = open('output.ics', 'wb')
    f.write(process_cal.to_ical())
    f.close()
    
if __name__ == '__main__':
    cal = sys.argv[1]
    year = int(sys.argv[2])
    month = int(sys.argv[3])
    day = int(sys.argv[4])
    dt = date(year, month, day)
    convert_calendar(cal, dt)