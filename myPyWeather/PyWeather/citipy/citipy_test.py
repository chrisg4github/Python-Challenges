# #!pip install citipy
# #https://pypi.python.org/pypi/citipy
# #https://github.com/wingchen/citipy 

from citipy import citipy as cp

# #New York, New York, USA
#city = cp.nearest_city(40.73, -73.94)

# #Quimper,fr
# #city = cp.nearest_city(48.0, -4.1)

# #Tainan, Taiwan  # tainan,tw my home town
# #city = cp.nearest_city(22.99, 120.21)

# #Yako, bf
# #city = cp.nearest_city(12.95, -2.26)

# #Wellington,?
# #city = cp.nearest_city(-41.28, 174.77)

# #San Francisco, CA, USA
# #city = cp.nearest_city(37.77, -122.43)

# #Sacramento, CA, USA
# #city = cp.nearest_city(38.58, -121.48)

# San Ramon, CA, USA
city = cp.nearest_city(37.80,-121.98)


print(city.city_name)     
print(city.country_code)            

# #----------------------------------------------------

# #Test: random.uniform coordinates and city lookup

# from citipy import citipy as cp
# from random import uniform

# # Testing one geo coordinate pair
# x,y = uniform(-90, 90),uniform(-180,-90) 
# print(x)
# print(y)
# print()

# # Test Looking up coordinates city, country
# city = cp.nearest_city(x, y)
# print(city.city_name)     
# print(city.country_code)  

#------------------------------------------------------------------

#import citipy
#import unittest
#
#
#class TestNearestCity(unittest.TestCase):
#    def test_tainan(self):
#        city = citipy.nearest_city(22.99, 120.21)
#        self.assertEqual('tainan', city.city_name)
#
#    def test_Quimper(self):
#        city = citipy.nearest_city(48.0, -4.1)
#        self.assertEqual('quimper', city.city_name)
#
#    def test_Yako(self):
#        city = citipy.nearest_city(12.95, -2.26)
#        self.assertEqual('yako', city.city_name)
#
#    def test_NewYork(self):
#        city = citipy.nearest_city(40.78, -73.96)
#        self.assertEqual('edgewater', city.city_name)
#
#    def test_Wellington(self):
#        city = citipy.nearest_city(-41.28, 174.77)
#        self.assertEqual('wellington', city.city_name)
#
#if __name__ == '__main__':
#unittest.main()
