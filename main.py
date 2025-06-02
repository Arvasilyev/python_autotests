import requests

# Константы
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5fe38f253e563a273d76a2879a19238e'

# Заголовки запросов
HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}

# Создание нового покемона
CREATE_POKEMON_BODY = {"name": "generate", "photo_id": -1}
response_create_pokemon = requests.post(url=f'{URL}/pokemons', headers=HEADERS, json=CREATE_POKEMON_BODY)

# Получение ID созданного покемона
pokemon_id = response_create_pokemon.json()['id']
print("ID созданного покемона:", pokemon_id)

# Получение информации о покемоне по ID
response_get_pokemon = requests.get(url=f'{URL}/pokemons/{pokemon_id}')
print("Имя созданного покемона:", response_get_pokemon.json()['name'])

# Переименование покемона
RENAME_POKEMON_BODY = {"pokemon_id": pokemon_id, "name": "generate", "photo_id": -1}
response_rename_pokemon = requests.put(url=f'{URL}/pokemons', headers=HEADERS, json=RENAME_POKEMON_BODY)
print(response_rename_pokemon.json()['message'])

# Повторно получаем данные, чтобы увидеть новое имя
response_get_pokemon = requests.get(url=f'{URL}/pokemons/{pokemon_id}')
print("Новое имя покемона:", response_get_pokemon.json()['name'])

# Помещение покемона в покебол
ADD_TO_POKEBALL_BODY = {"pokemon_id": pokemon_id}
response_add_to_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADERS, json=ADD_TO_POKEBALL_BODY)
print(response_add_to_pokeball.json()['message'])