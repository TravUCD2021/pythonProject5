import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

data=pd.read_csv("Month.csv")

print(data)

y=data["date_time"]
x=data["amount"]

fig, ax = plt.subplots()
ax.plot(x,y)

ax.set(xlabel='Value', ylabel='Dates',
       title='USD Payments')
ax.grid()


plt.show()

