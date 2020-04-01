"""
 The program converts the given date and time into Unix timestamp (Made: Jauaries Loyala -- 9.01.2020).
"""

# Python packets
import datetime
import time
import argparse

from datetime import timezone


"""
 In the terminal the arguments are given in the following form:
    python3 unixtime.py YYYY-MM-DD HH:MM:SS
 Due note that the year can be either given in form of '2020' or '20', the datetime function reads this still as year 2020.
"""

# Giving the arguments in the terminal
parser = argparse.ArgumentParser()

# The wanted parser arguments (date & time)
parser.add_argument("date", help = "Date to generate unix timestamp (format YYYY-MM-DD)")
parser.add_argument("time", help = "Time to generate unix timestamp (format HH:MM:SS)")

args = parser.parse_args()

date = args.date
date_time = args.time

# Transforming the arguments values into integer form
year, month, day = map(int, date.split('-'))
hour, minute, second = map(int, date_time.split(':'))


# Date
date_time = datetime.datetime(year, month, day, hour, minute)
print(date_time)


# Converting the local time and UTC time into unix timestamp
unix_time_local = int(time.mktime(date_time.timetuple()))
#unix_time_UTC = int((dt - datetime.datetime(1970, 1, 1, 0, 0)).total_seconds()) # Python 2
unix_time_UTC = int(date_time.replace(tzinfo = timezone.utc).timestamp()) # Python 3


# Printing the output
print("Unix Timestamp (Local): %s" %unix_time_local)
print("Unix Timestamp (UTC): %s" %unix_time_UTC)

