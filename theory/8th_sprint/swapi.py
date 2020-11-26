import requests
from pprint import pprint


result = requests.get('https://swapi.dev/api/people/').json()['results'][:3]
pprint(result)

planet = requests.get('https://swapi.dev/api/people/?search=luke').json()['results'][0]['homeworld']
result = requests.get(planet).json()['diameter']

print(result)