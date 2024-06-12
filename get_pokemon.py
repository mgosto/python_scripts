import requests
import random
  # Get user input
set_number = int(input("Enter the number of users to create: "))

while set_number >= 0:
    ran_number = random.randint(1, 1302)  # Range from 1 to 1302

    url = f"https://pokeapi.co/api/v2/pokemon/{ran_number}"

    # Get list of pokemon
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"name: {data['name']}")
    set_number -= 1
