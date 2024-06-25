# Which Year is This? exercise in Reading Documentation 2 exercises:

"""The Python documentation for the datetime module provides two 
attributes to retrieve the year from a date or datetime object: year and 
isocalendar.

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

What is the difference between the year attribute and the isocalendar 
method?
"""


from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]
iso = today.isocalendar()

print(today)
print(today_year)
print(iso_year)
print(iso)


"""
'The ISO calendar is a widely used variant of the Gregorian calendar.'
https://docs.python.org/3/library/datetime.html#examples-of-usage-datetime

I can't work out the exact details from the documentation.
"""


"""The given solution indicates that the the year attribute of a date or 
datetime object simply returns the year of that date, whereas the 
isocalendar method returns a tuple of three values: the ISO year, the
ISO week number, and the ISO weekday. This may differ from the Gregorian
calendar toward the beginning/end of the year due to how they're 
calculated (the ISO year starts with the first week that has at least 4
days in the new year. More common to just use the year attribute.)
"""