#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

# Load in the data
mydata = pd.read_csv("data.csv", header=0)

# Perform calculations.
mydata['mean'] = mydata.mean(axis=1)
mydata['dilution_corrected'] = mydata['mean']*100
mydata['cells_per_ml'] = mydata['dilution_corrected']*300000

# Make a plot.
fig, ax = plt.subplots()
strains = ['Strain 1', 'Strain 2', 'Strain 3', 'Strain 4']
values = mydata['cells_per_ml']
ax.bar(strains,values)
plt.show()