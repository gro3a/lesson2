import ephem
import datetime

def name_planet():
    planet=input('Name planet: ')
    date= datetime.datetime.now()
    result=''
    if planet == "Earth":
        result = ephem.constellation(ephem.Earth(date))
    elif planet == 'Mercury':
    	result = ephem.constellation(ephem.Mercury(date))
    elif planet == 'Venus':
    	result = ephem.constellation(ephem.Venus(date))
    elif planet == 'Mars':
    	result = ephem.constellation(ephem.Mars(date))
    elif planet == 'Jupiter':
    	result = ephem.constellation(ephem.Jupiter(date))
    elif planet == 'Saturn':
    	result = ephem.constellation(ephem.Saturn(date))
    elif planet == 'Uranus':
    	result = ephem.constellation(ephem.Uranus(date))
    elif planet == 'Neptune':
    	result = ephem.constellation(ephem.Neptune(date))
    return result
    
print(name_planet())


