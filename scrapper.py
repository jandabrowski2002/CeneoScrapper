import requests
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/67071831#tab=reviews"

response = requests.get(url)

page_dom = BeautifulSoup(response.text, "html.parser")

opinions = page_dom.select("div.js_product-review")
opinion = opinions.pop()

opinion_id = opinion["data-entry-id"]
author = opinion.select_one("span.user-post__author-name").text.strip()
rcmd = opinion.select_one("span.user-post__author__recomendation").text.strip()
score = opinion.select_one("span.user-post__score-count").text.strip()
content = opinion.select_one("div.user-post__text").text.strip()
pros = opinion.select_one("div.review-feature__title--positives ~ div.review-feature__Item").text.strip()
cons = opinion.select_one("div.review-feature__title--negatives ~ div.review-feature__Item").text.strip()
posted_on = opinion.select_one("span.user-post__published > time:nth-child(1)\["datetime"\]").text.strip()



print(type(author))
print(author)