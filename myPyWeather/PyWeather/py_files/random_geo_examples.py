# random geo coordinate generator
# http://hadoopguru.blogspot.com/2014/12/python-generate-random-latitude-and.html

#==================================================================
#import random
#import sys
#import math
#
#outfile = open("output\randomLatLong_NY.txt", "w")
#
#radius = 10000                         #Choose your own radius
#radiusInDegrees=radius/111300            
#r = radiusInDegrees
#x0 = 40.84
#y0 = -73.87
#
#for i in range(1,100): #Choose number of Lat Long to be generated
#
#  u = float(random.uniform(0.0,1.0))
#  v = float(random.uniform(0.0,1.0))
#
#  w = r * math.sqrt(u)
#  t = 2 * math.pi * v
#  x = w * math.cos(t) 
#  y = w * math.sin(t)
#  
#  xLat  = x + x0
#  yLong = y + y0
#  outfile.write (str(xLat) + "," + str(yLong) + '\n')

#==================================================================
import random
import sys
import math

# random.seed(a=None, version=2)

#latitude = 19.99
#longitude = 73.78
#output_file = 'filename'
#
#def generate_random_data():
#    with open(output_file, 'w') as output:
#        hex1 = '%012X' % random.randint(0,100)
#        flt = float(random.randint(0,100))
#        latitude = math.acos(random.random() * 2 - 1)
#        longitude = random.random() * math.pi * 2
#
#        output.write('%s %.1f %.6f %.6f \n' % (hex1.lower(), 
#                                               flt, longitude, 
#                                               latitude))
    
from random import uniform
x, y = uniform(-180,180), uniform(-90, 90)
    
    
    
    
    
    
    