import requests

HEADER = {'Content-Type': 'application/json',
          'trainer_token':'ecaae1791f8b6b0366af6c2064fc04c7'}

body_new = {
    "name": "generate",
    "photo": "generate"
}

body_name = {
    "pokemon_id": "29636",
    "name": "Злодей",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_pokebol = {
    "pokemon_id": "29636"
}

response = requests.post('https://api.pokemonbattle.me:9104/pokemons', json=body_new, headers=HEADER)
print(response.text)

response = requests.put('https://api.pokemonbattle.me:9104/pokemons', json=body_name, headers=HEADER)
print(response.text)

response = requests.post('https://api.pokemonbattle.me:9104//trainers/add_pokeball', json=body_pokebol, headers=HEADER)
print(response.text)