import requests

# Getting user input for which pokemon to look up
# I used the endpoint that needed a pokemon name
# but there are many, many more endpoints.
name = input('What pokemon do you want? : ')

# Think of this as accessing the data found at that endpoint.
response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')

# Getting the url response and reading it in JSON format
pokemon_info = response.json()

# Now it's just simple dictionary work to collect data
name = pokemon_info['name']
weight = pokemon_info['weight']

# Printing is obviously pretty lame -- but we'll do more with matplotlib
print(name, weight)