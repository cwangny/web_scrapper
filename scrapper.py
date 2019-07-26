#Sydney weather data scrapper 

#can use urllib(pre-installed) library or requests 
#from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import requests 

#7 DAYS FORECAST

my_url = 'https://www.weather.com.au/nsw/sydney'

#opening up connection and grabbing the page

'''
uClient = uReq(my_url) #uReq opens up a connection to the server and to the client 
raw_html = uClient.read()
uClient.close()
'''

source = requests.get(my_url) #establishes the link. can also use this [requests.get(my_url).text]
raw_html = source.text #converts into a text file which can be parsed

#HTML parsing
webpage = soup(raw_html, 'html.parser')
#print(webpage.prettify()) Test

forecast = {}

day_list = []
#find returns the first result that matches the argument, find_all returns a list of all results.
for day in webpage.find_all('td', class_ = 'day'): #class is a reserved word, use class_ instead
	day_list.append(day.text)

forecast_list = []
for forecast in webpage.find_all('td', class_ = 'forecast'):
	forecast_list.append(forecast.text)

min_list = []
for min_ in webpage.find_all('td', class_ = 'min'):
	min_list.append(min_.text)

max_list = []
for max_ in webpage.find_all('td', class_ = 'max'):
	max_list.append(max_.text)

min_max_list = zip(min_list, max_list)

values_list = zip(forecast_list, min_max_list)


forecast = dict(zip(day_list, values_list))

#INPUTS: 
#MON TUE WED THU FRI SAT SUN 

#print(forecast['SUN'])	

#CURRENT FORECAST

current_url = 'https://www.weather.com.au/nsw/sydney/current'

source_c = requests.get(current_url).text

webpage_c = soup(source_c, 'html.parser')

var_list = []
for data in webpage_c.find_all('td', class_ = 'var'):
	var_list.append(data.text)

#print(var_list)

val_list = []
for data in webpage_c.find_all('td', class_ = 'val'):
	val_list.append(data.text)

#print(val_list)

current_dict = dict(zip(var_list, val_list))#creates a dictionary

'''
INPUTS:

Temperature
Dew Point
Relative Humidity
Wind Speed
Wind Gusts
Wind Direction
Pressure
Rain Since 9AM
'''

print(current_dict['Temperature'])






















