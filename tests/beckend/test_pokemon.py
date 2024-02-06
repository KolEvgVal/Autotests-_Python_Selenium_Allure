import requests
import pytest


HEADER = {'Content-Type': 'application/json',
          'trainer_token':'ecaae1791f8b6b0366af6c2064fc04c7'}

def test_get_trainers():
 """
 KTI-1. Get trainers
 """
 response = requests.get('https://api.pokemonbattle.me:9104/trainers', timeout=5)
 assert response.status_code == 200, 'Unexpected status code'


def test_get_trainers_id_3663():
 """
 KTI-2. Get trainers by id
 """
 response = requests.get('https://api.pokemonbattle.me:9104/trainers', params={'trainer_id': 3663}, timeout=5)
 assert response.json()['trainer_name'] == 'Sub-zero'