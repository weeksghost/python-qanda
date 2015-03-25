"""Write a function named time_machine
that takes an integer and a string of
"minutes", "hours", "days", or "years".
This describes a timedelta.
Return a datetime that is the timedelta's duration
from the starter datetime."""

# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)

import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)


def time_machine(num, string):
    td = ()
    if string == "years":
        td = datetime.timedelta(days=(num*365))
    elif string == "minutes":
        td = datetime.timedelta(minutes=num)
    elif string == "hours":
        td = datetime.timedelta(hours=num)
    elif string == "days":
        td = datetime.timedelta(days=num)
    return starter + td

print(time_machine(10, "years"))