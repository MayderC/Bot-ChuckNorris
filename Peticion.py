import requests
import json
from mtranslate import translate


def peticion():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.request('GET', url=url)
    response = json.loads(response.text)

    #Traduce el mensaje a español
    value = translate(response['value'], 'es')
    
    return value

    #obtener respuesta en inglés
def req():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.request('GET', url=url)
    response = json.loads(response.text)

    value = (response['value'])
    
    return value
