import numpy as np
from datetime import datetime as dt

# empty dictionary to hold receipt data
data = {}

# limit year to four digits
year = int(input('Enter year: '))
# must be 1-12
month = int(input('Enter month: '))
# must be 1 - 31 and better yet depending on the month
day = int(input('Enter day: '))

def add_receipt(year, month, day):
    new_receipt = dt(year, month, day).strftime('%d-%m-%y')
    