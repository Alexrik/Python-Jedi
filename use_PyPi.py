

import pyowm

city = input ('Temperature of what city you interesting in now?: ')

owm = pyowm.OWM ('d2f55bb3a608a267c91d7128e6370514')
observation = owm.weather_at_place(city)
w = observation.get_weather()
temper = w.get_temperature('celsius')['temp']

print ('in city' + city + 'that temperature' + str(temperature))
#print (w)