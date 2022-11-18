import requests


response = requests.post("https://coinmarketcap.com", data="Text data", headers={"h1:Test title"})
print(response.text)