import requests
import pytest

URL='https://api.pokemonbattle.ru/v2'
TRAINER_ID='33560'
HEADER={
    'Content-Type' : 'application/json'
}

# Проверка кода
def test_status_code():
    response_status_code = requests.get(url=f'{URL}/trainers/{TRAINER_ID}')
    assert response_status_code.status_code == 200

# Проверка имени
def test_trainer_name():
    response_trainer_name = requests.get(url=f'{URL}/trainers/{TRAINER_ID}')
    assert response_trainer_name.json()['trainer_name'] == 'ArtBasilio'