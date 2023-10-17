import requests

url = 'https://api.mts.ru/token'
#auth = ('', '') - Здесь нужно прописать логин и пароль, полученные во вкладке API
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {'grant_type': 'client_credentials', 'validity_period': '1800'}

response = requests.post(url, auth=auth, headers=headers, data=data)
resp = response.json()

token =  resp['access_token']

headers = {'Authorization': 'Bearer ' + token}
params = {'fields': 'MOAF', 'accountNo': 'номер_счета'}

response = requests.get('https://api.mts.ru/b2b/v1/Bills/CheckBalanceByAccount', headers=headers, params=params)

print(response.text)




