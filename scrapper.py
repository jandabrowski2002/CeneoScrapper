from textwrap import indent
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.ceneo.pl/67071831#tab=reviews"
all_opinions = []
while(url):
    response = requests.get(url)
    page_dom = BeautifulSoup(response.text, "html.parser")
    opinions = page_dom.select("div.js_product-review")

    for opinion in opinions:
        opinion_id = opinion["data-entry-id"]
        author = opinion.select_one("span.user-post__author-name").text.strip()
        try:
            rcmd = opinion.select_one("span.user-post__author__recomendation").text.strip()
        except AttributeError:
            rcmd = None
        score = opinion.select_one("span.user-post__score-count").text.strip()
        content = opinion.select_one("div.user-post__text").text.strip()
        try:
            pros = opinion.select("div.review-feature__title--positives ~ div.review-feature__Item")
            pros = [item.text.strip() for item in pros]
        except AttributeError:
            pros = None
        try:
            cons = opinion.select("div.review-feature__title--negatives ~ div.review-feature__Item")
            cons = [item.text.strip() for item in cons]
        except AttributeError:
            cons = None
        posted_on = opinion.select_one("span.user-post__published > time:nth-child(1)")(["datetime"])
        bought_on = opinion.select_one("span.user-post__published > time:nth-child(2)")(["datetime"])
        useful_for = opinion.select_one("button.vote-yes > span").text.strip()
        useless_for = opinion.select_one("button.vote-no > span").text.strip()

        single_opinion = {
            "opinion_id": opinion_id,
            "author": author,
            "rcmd": rcmd,
            "score": score,
            "content": content,
            "posted_on": posted_on,
            "bought_on": bought_on,
            "useful_for": useful_for,
            "useless_for": useless_for,
            "pros": pros,
            "cons": cons,
        }
        all_opinions.append(single_opinion)

    try:
        url = "https://www.ceneo.pl/" + page_dom.select_one("a.pagination__next")["href"]
    except TypeError:
        url = None

with open("opinions/67071831.json", "w", encoding="UTF-8") as jf:
    print(json.dumps(all_opinions, indent = 4, ensure_ascii = False))

