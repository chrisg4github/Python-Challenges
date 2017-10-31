# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 22:00:20 2017
"""
# This program from: 
# http://glowingpython.blogspot.com/2011/11/how-to-make-bubble-charts-with.html

#------------------ uncomment only single hash marks --------------
#from pylab import *
#from scipy import *
#
## reading the data from a csv file
##durl = 'http://datasets.flowingdata.com/crimeRatesByState2005.csv'
#durl = '../data/crimeRatesByState2005.csv'
#rdata = genfromtxt(durl,dtype='S8,f,f,f,f,f,f,f,i',delimiter=',')
##print(rdata)
#
#rdata[0] = zeros(8) # cutting the label's titles
#rdata[1] = zeros(8) # cutting the global statistics
#
#x = []
#y = []
#color = []
#area = []
#
#for data in rdata:
# x.append(data[1]) # murder
# y.append(data[5]) # burglary
# color.append(data[6]) # larceny_theft 
# area.append(sqrt(data[8])) # population
# # plotting the first eigth letters of the state's name
# text(data[1], data[5], 
#      data[0],size=11,horizontalalignment='center')
#
## making the scatter plot
#sct = scatter(x, y, c=color, s=area, linewidths=2, edgecolor='w')
#sct.set_alpha(0.75)
#
#axis([0,11,200,1280])
#xlabel('Murders per 100,000 population')
#ylabel('Burglaries per 100,000 population')
#show()

#-----------------------------------------------------------------------------
# from url: https://plot.ly/matplotlib/bubble-charts/
# This chart has bubble size impact

# Note: The Python API is a package designed to interact with 
# the Plotly.js library in order to allow Python users to create 
# plots in their preferred environment.

#------------------ uncomment only single hash marks --------------
#import matplotlib.pyplot as plt
## https://plot.ly/python/getting-started/
##import plotly.plotly as py   # not installed
#
#bubbles_mpl = plt.figure()
#
## doubling the width of markers
#x = [0,2,4,6,8,10]
#y = [0]*len(x)
#s = [20*4**n for n in range(len(x))]
#
#plt.savefig("bubble_growth.png")
##plot_url = py.plot_mpl(bubbles_mpl, filename='mpl-bubbles')
#
#plt.scatter(x,y,s=s)
#plt.savefig("bubble_growth.png")
##plt.show()


#-----------------------------------------------------------------------------
# from url: https://plot.ly/matplotlib/bubble-charts/
# This chart has bubble chart size impact

#------------------ uncomment only single hash marks --------------
import matplotlib.pyplot as plt
import numpy as np
## https://plot.ly/python/getting-started/
#import plotly.plotly as py  # not installed

n = 50
x, y, z, s, ew = np.random.rand(5, n)

c, ec = np.random.rand(2, n, 4)

area_scale, width_scale = 500, 5

fig, ax = plt.subplots()

sc = ax.scatter(x, y, s=np.square(s)*area_scale, c=c, edgecolor=ec, 
                linewidth=ew*width_scale)
ax.grid()

plt.savefig("bubble_scatter.png")
plt.show()
#plot_url = py.plot_mpl(fig, filename='mpl-7d-bubble')

#-----------------------------------------------------------------------------
# Same plot as the one directly above but this has seaborn elements
# example bubble chart for help
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
np.random.seed(sum(map(ord, "aesthetics")))
## https://plot.ly/python/getting-started/
#import plotly.plotly as py  # not installed

n = 50
x, y, z, s, ew = np.random.rand(5, n)

c, ec = np.random.rand(2, n, 4)

area_scale, width_scale = 500, 5

fig, ax = plt.subplots()

sc = ax.scatter(x, y, s=np.square(s)*area_scale, c=c, edgecolor=ec, 
                linewidth=ew*width_scale)
#ax.grid()
sns.set_style("darkgrid")

plt.savefig("./chart_images/bubble_scatter.png")
plt.show()

















