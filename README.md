# UnixTime

Some of the satellites use UTC time in unix timestamp format instead of normal time form like UTC 11:00:00. In order to define the corret unix timestamp, satellite operator has to calculate the UTC time from the local time and search a convertor from the online to convert it to timestamp.


Project includes of twp python programs:

    - unixtime.py
    - timestamp_to_UTC.py

The first program converst date and time into Unix timestamp and prints both the local version and the UTC version of the timestamp. Second program converts timestamp it to UTC date and time.
