import requests
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/67071831#tab=reviews"

response = requests.get(url)

page_dom = BeautifulSoup(response.text, "html.parser")

opinions = page_dom.select("div.js_product-review")

opinion = opinions.pop()

print(type(opinion.prettify()))