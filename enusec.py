import requests
response = requests.post('http://ctf1.enusec.org/', data={"malone"})
print(response.text)