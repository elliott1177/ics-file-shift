# ics-file-shift

Shift the events on a ics calendar by a specified parameter (Date)

# How to use:

1. Clone or download this repository onto your machine.
2. Open up a terminal and change into the directory that this repository is stored in. `cd ics-file-shift`
3. Make sure you have Python 3.x installed as well as pip.
4. Copy the calendar you want shifted into the ics-file-shift directory.
5. Run: `pip install -r requirements.txt`
6. Compile the script with: `chmod +x date_conversion.py`
7. To shift the calendar: `./date_conversion.py calendar.ics year month date`
8. calendar.ics is the calendar you want to shift. year month and date is the date you want the first calendar event to be on eg. 2020 05 15
9. After running your shifted calendar will be contained in **ouput.ics**
