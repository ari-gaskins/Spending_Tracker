import numpy as np
from datetime import datetime as dt

# raw date and total cost data from receipts
data = {dt(2022, 10, 7): 5.99, dt(2022, 10, 6): 5.00, dt(2022, 10, 3): 2.50,
        dt(2022, 10, 1): 23.51, dt(2022, 10, 1): 12.41, dt(2022, 9, 30): 16.43,
        dt(2022, 9, 28): 3.18, dt(2022, 9, 25): 17.68, dt(2022, 9, 22): 79.01,
        dt(2022, 9, 14): 1.06, dt(2022, 9, 13): 1.06, dt(2022, 9, 6): 21.33,
        dt(2022, 9, 5): 6.77, dt(2022, 9, 1): 10.20, dt(2022, 9, 1): 31.25,
        dt(2022, 8, 4): 4.34, dt(2022, 8, 26): 73.17, dt(2022, 8, 29): 10.24,
        dt(2022, 8, 23): 5.12, dt(2022, 8, 22): 2.12, dt(2022, 8, 21): 1.06,
        dt(2022, 8, 10): 2.12, dt(2022, 8, 21): 1.06, dt(2022, 8, 9): 11.88,
        dt(2022, 8, 9): 2.12, dt(2022, 8, 8): 1.06, dt(2022, 8, 8): 1.06,
        dt(2022, 8, 21): 1.06, dt(2022, 8, 20): 2.12}

# creating numpy arrays from data
# check dtype of datetime
keys = np.fromiter(data.keys(), dtype=type)

values = np.fromiter(data.values(), dtype=float)

# strftime is a function of dt, must use for each object to return as string
print(dt(2022, 10, 7).strftime('%d-%m-%y'))