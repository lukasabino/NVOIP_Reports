#import needed modules
import requests, time, json, sys
from datetime import date

from requests.api import head

#loads variables from json files
try:
    variaveis = json.load(open('variables.json', 'r'))
    chaves = json.load(open('keys.json', 'r', encoding='utf8'))
    if variaveis['arg'] not in chaves['data']:
        with open('variables.json', 'w') as write_file:
            variaveis['report'] = 'You sent an incorrect command'
            json.dump(variaveis, write_file)
            sys.exit()
except Exception as e:
    with open('variables.json', 'w') as write_file:
        variaveis['report'] = 'An error ocourred'
        json.dump(variaveis, write_file)
        sys.exit()

#request to API
headers = {
	'Content-Type': 'application/json',
	'token_auth': chaves['nvoip_token']
}
URL = 'https://api.nvoip.com.br/v1/balance'
page = requests.get(URL, headers=headers)

#json from API response
lista = page.json()
print(lista)

#creates time and date objects
hoje = date.today()
t = time.localtime()
hora = time.strftime("%H:%M", t)

#converts number to name of months
def mes(arg):
	if arg == 1:
		return "janeiro"
	if arg == 2:
		return "fevereiro"
	if arg == 3:
		return "março"
	if arg == 4:
		return "abril"
	if arg == 5:
		return "maio"
	if arg == 6:
		return "junho"
	if arg == 7:
		return "julho"
	if arg == 8:
		return "agosto"
	if arg == 9:
		return "setembro"
	if arg == 10:
		return "outubro"
	if arg == 11:
		return "novembro"
	if arg == 12:
		return "dezembro"

#counts the calls -- comming soon
def call_count(jsonobj):
	est = 0
	for ticket in jsonobj['data']:
		if ticket['finished']:
			pass
		else:
			est += 1
	return est

#creates the message string
mensagem = open('model.txt', 'r', encoding='utf8').read()
mensagem = mensagem.replace('{balance}', str(lista['balance']))

#dumps the message into the variables json
variaveis['report'] = mensagem
with open('variables.json', 'w', encoding='utf8') as write_file:
    json.dump(variaveis, write_file)