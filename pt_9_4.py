import requests
from bs4 import BeautifulSoup


resp = requests.get("https://bank.gov.ua/ua/markets/exchangerates/")
if resp.status_code == 200:
    soup =  BeautifulSoup(resp.text, features="html.parser")
    soup_list = soup.find_all("a", {"href":"/currencies/грн /markets/"})
    res = soup_list[839].find("span")
    print(res.text)
