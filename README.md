# CeneoScrapper

# Single opinion structure

|Element|Selector|Variable|
|-------|--------|--------|
|Opinion|div.js_product-review|opinion|
|Opinion id|\["data-entry-id"\]|opinion_id|
|Author|span.user-post_author-name|author|
|Reomendation|span.user-post__author__recomendation > en|rcmd|
|Stars score|span.user-post__score-count|score|
|Content|div.user-post__text|content|
|List of advantages|div.review-feature__title--positives ~ div.review-feature__Item|pros|
|List of disadvantages|div.review-feature__title--negatives ~ div.review-feature__Item|cons|
|Date of posting poinion|span.user-post__published > time:nth-child(1)\["datetime"\]|posted_on|
|Date of purchasing product|span.user-post__published > time:nth-child(2)\["datetime"\]|bought_on|
|For how many users useful|button.vote-yes > span|useful_for|
|For how many users useless|button.vote-no > span|useless_for|

# Stages of project

1) Extraction of elements for a single