import requests
URL = 'https://api.pokemonbattle.me'
path = '/v2/pokemons'
trainer_token = {'68d6c5372adcedc4d6828dc39adf89ed'}
HEADER = {'Content-Type':'application/json', 'trainer_token':'68d6c5372adcedc4d6828dc39adf89ed'}
body = {
    "name" : "Бульбуль",
    "photo": "https://dolnikov.ru/pokemons/albums/009.png"
}
responce=requests.post(url=f'{URL}/v2/pokemons', json=body, headers=HEADER, timeout=10)
print(responce)

import requests
URL = 'https://api.pokemonbattle.me'
path = '/v2/pokemons'
trainer_token = {'68d6c5372adcedc4d6828dc39adf89ed'}
HEADER = {'Content-Type':'application/json', 'trainer_token':'68d6c5372adcedc4d6828dc39adf89ed'}
body = {
    "pokemon_id": "17321",
    "name": "Домовой",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
responce=requests.put(url=f'{URL}/v2/pokemons', json=body, headers=HEADER, timeout=10)
print(responce)

import requests
URL = 'https://api.pokemonbattle.me'
path = '/v2/trainers/add_pokeball'
trainer_token = {'68d6c5372adcedc4d6828dc39adf89ed'}
HEADER = {'Content-Type':'application/json', 'trainer_token':'68d6c5372adcedc4d6828dc39adf89ed'}
body = {
    "pokemon_id": "17321"
}
responce=requests.put(url=f'{URL}/v2/trainers/add_pokeball', json=body, headers=HEADER, timeout=10)
print(responce)