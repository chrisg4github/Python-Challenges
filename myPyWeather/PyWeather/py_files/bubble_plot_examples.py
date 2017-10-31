
#https://stackoverflow.com/questions/26139423/plot-different-color-for-different-categorical-levels-using-matplotlib

# The following two plots came from the above url

import matplotlib.pyplot as plt
import pandas as pd

carat = [5, 10, 20, 30, 5, 10, 20, 30, 5, 10, 20, 30]
price = [100, 100, 200, 200, 300, 300, 400, 400, 500, 500, 600, 600]
color =['D', 'D', 'D', 'E', 'E', 'E', 'F', 'F', 'F', 'G', 'G', 'G',]

df = pd.DataFrame(dict(carat=carat, price=price, color=color))

fig, ax = plt.subplots()

colors = {'D':'red', 'E':'blue', 'F':'green', 'G':'black'}

ax.scatter(df['carat'], df['price'], c=df['color'].apply(lambda x: colors[x]))

plt.show()



# http://seaborn.pydata.org/generated/seaborn.lmplot.html

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

carat = [5, 10, 20, 30, 5, 10, 20, 30, 5, 10, 20, 30]
price = [100, 100, 200, 200, 300, 300, 400, 400, 500, 500, 600, 600]
color =['D', 'D', 'D', 'E', 'E', 'E', 'F', 'F', 'F', 'G', 'G', 'G',]

df = pd.DataFrame(dict(carat=carat, price=price, color=color))

sns.lmplot('carat', 'price', data=df, hue='color', fit_reg=False)

plt.show()


# my adaptation of the above plots

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# all lists should have 125 elements
x_fare = average_fare[avg_fare]
y_ride = total_rides[ride_count]

# color is defined by the type in colors
ctype = city_type_df[type].apply(lambda x: colors[x])

colors = {"rural":"gold", "suburban":"coral", "urban":"skyblue"}


# Not sure how to create this size modification of the dcount_df
#size calc = 100 * (iris.petal_length - iris.petal_length.min()) 
# #/ (iris.petal_length.max() - iris.petal_length.min()))
# #df = pd.DataFrame(dict(carat=carat, price=price, color=color))

dcnt = dcount_df[driver_count].apply(lambda x: 


df = pd.DataFrame(dict(x=x, y=y, color=type, size=dcnt))

sns.lmplot('x', 'y', data=df, hue='color', size=dcnt, fit_reg=False)

plt.show()





# # from url: https://plot.ly/matplotlib/bubble-charts/
# 
# # http://matplotlib.org/api/markers_api.html?highlight=marker
# #
# #------------------ uncomment only single hash marks --------------
# # https://plot.ly/python/getting-started/
# #import plotly.plotly as py  # not installed

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# all lists should have 125 elements
x_fare = average_fare[avg_fare]
y_ride = total_rides[ride_count]

# color is defined by the type in colors
colors = {"rural":"gold", "suburban":"coral", "urban":"skyblue"}
ctype = city_type_df[type].apply(lambda x: colors[x])

fig, ax = plt.subplots()


ax.set_title("Pyber Ride Sharing Data (2016)")
ax.set_xlabel("Total Number of Rides (Per City)")
ax.set_ylabel("Average Fare ($)")

# # Not sure how to create this size modification of the dcount_df
# #size calc = 100 * (iris.petal_length - iris.petal_length.min()) 
# # #/ (iris.petal_length.max() - iris.petal_length.min()))
# # #df = pd.DataFrame(dict(carat=carat, price=price, color=color))
# #dcnt = dcount_df[driver_count].apply(lambda x: 

# df = pd.DataFrame(dict(x=x, y=y, color=type, size=dcnt))
# sns.lmplot('x', 'y', data=df, hue='color', size=dcnt, fit_reg=False)

# sns.set_style("darkgrid")

# plt.savefig("bubble_scatter_example.png")
# plt.show()
# plt.show()












# x = total_rides["ride_count"]
# y = average_fare["avg_fare"]
# s = dcounts_df["driver_count"]  

# colors = ["gold", "coral", "skyblue"]

# fig, ax = plt.subplots()


# ax.set_title("Pyber Ride Sharing Data (2016)")
# ax.set_xlabel("Total Number of Rides (Per City)")
# ax.set_ylabel("Average Fare ($)")

# # Bubble chart relations
# # x is total rides, y is average fares 
# # colors are related to type
# # driver count is related to bubble size

# # first attempt
# #sc = ax.scatter(x, y, marker="o", markersize=driver_count, c=colors, edgecolor=c, linewidth=0)
# #sc = ax.scatter(x, y, marker="o", c="red", linewidth=0)
# sc = ax.scatter(x, y, marker="o", linewidth=0)

# # for the legend - relate type  colors to type, marker "o"
# ax.legend(["City Types","Rural"], loc=1)
# #ax.grid()
# sns.set_style("darkgrid")

# plt.savefig("bubble_scatter_example.png")
# plt.show()






