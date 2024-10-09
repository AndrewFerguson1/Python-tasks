import requests
x = requests.get('http://ctf1.enusec.org/')
print(x.status_code)

response = requests.post('http://ctf1.enusec.org/', data={"malone"})
print(response.text)