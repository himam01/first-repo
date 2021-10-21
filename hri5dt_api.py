# hri5dt
# Heba Imam
# I apologize for submitting this late: I ran into issues with installing the requests module which took me a while to figure out and therefore I ended up 
# needing more time to do the assignment than I had allotted
# the following lines of code are lines I typed, but they are based off the tutorial I watched for
# learning the syntax and how to use the yelp API with python, which is linked here: https://www.youtube.com/watch?v=GJf7ccRIK4U

# below are the modules I imported based on the modules listed in the tutorial to import
import requests
import json

# I learned the syntax for all of the following code from the youtube tutorial linked above

my_id = 'PhqaQXtp8Nd3x0Y6SbpdSA' 

API_KEY = 'FeyEW4t7_gya0RUQ1pZgrLcDNMWWC7mDLjsUW8xWhIZ1IiPyKLzGmvngsLex8e5Br5BDxyb1XmdC9U_X4pQOJqROdCk5ppRIeVDOSnk2xX6vLEXB4ZBIL1vKue9wYXYx'
url = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'Bearer %s' % API_KEY}

# I decided to do the yelp api task idea that was given to us in the assignment, which was to find the seafood restaurants in one's city
# My hometown is Roanoke, Virginia; therefore, I set the term to seafood and the location to Roanoke, Virginia
PARAMETERS = {'term':'seafood', 'location': 'Roanoke, Virginia'}

result = requests.get(url, params = PARAMETERS, headers = HEADERS)

restaurant_info = result.json()

# I print out the seafood restaurant's name along with its rating
for restaurant in restaurant_info['businesses']:
    print(restaurant['name'], " ", restaurant['rating'])

