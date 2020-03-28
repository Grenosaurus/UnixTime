"""
 Program converts Unix timestamp into date (Made: Jauaries Loyala -- 15.01.2020)
"""

# Python packets
import argparse

from datetime import datetime


# Giving the arguments in the terminal
parser = argparse.ArgumentParser()

# The wanted parser arguments
parser.add_argument('unix') # Unix timestamp

args = parser.parse_args()


# Converting Unix timestamp into integer
unix_timestamp = int(args.unix)
#unix_timestamp = 1579003233


# Prints Unix timestamp into UTC date and time
print("Unix timestamp in UTC date: %s" %datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S'))

