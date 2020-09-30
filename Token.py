import json


def myToken():
    f = open('config.json', 'r')
    token = f.read()
    f.close()
    token = json.loads(token)
    token = token['config']['token']
    return token