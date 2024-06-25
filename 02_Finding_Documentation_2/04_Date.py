# Date exercise in Reading Documentation 2 exercises:

"""Using the datetime module in Python, how would you obtain the current 
date and time?
"""


import datetime 

current_date = datetime.datetime.now()
print(current_date)


"""
I had a really hard time figuring out how to make this work. The 
datetime.datetime.method() syntax isn't particularly clear in the 
documentation. I finally had to just look at the solution.

https://docs.python.org/3/library/datetime.html#examples-of-usage-datetime
https://docs.python.org/3/library/datetime.html#datetime.date.today
https://docs.python.org/3/library/datetime.html#examples-of-usage-date
https://docs.python.org/3/library/datetime.html#examples-of-usage-date
"""


"""The given solution mentions that "from datetime import datetime" is
more common and more readable. It explains that some modules contain
classes/functions with the same name as the module itself, which was 
very confusing when trying to interpret the documentation.
"""