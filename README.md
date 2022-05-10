# CeneoScrapper

# Single opinion structure

|Element|Selector|Variable|
|-------|--------|--------|
|Opinion|div.js_product-review|opinion|bs4.element.Tag|
|Opinion id|\["data-entry-id"\]|opinion_id|str|
|Author|span.user-post_author-name|author|str|
|Reomendation|span.user-post__author__recomendation > en|rcmd|bool|
|Stars score|span.user-post__score-count|score|float|
|Content|div.user-post__text|content|str|
|List of advantages|div.review-feature__title--positives ~ div.review-feature__Item|pros|list\[str\]|
|List of disadvantages|div.review-feature__title--negatives ~ div.review-feature__Item|cons|list\[str\]|
|Date of posting poinion|span.user-post__published > time:nth-child(1)\["datetime"\]|posted_on|str|
|Date of purchasing product|span.user-post__published > time:nth-child(2)\["datetime"\]|bought_on|str|
|For how many users useful|button.vote-yes > span|useful_for|int|
|For how many users useless|button.vote-no > span|useless_for|int|

# Stages of project



1) Extraction of elements for a single opinion to separate variables
2) Extraction of elements for a single opinion to one complex variable
3) Extraction of all opinions form single page to list
4) Extraction of all opinions for certain product and saving it to file
5) Code refactoring and optimiaztion
    a)Definition of function for etracting single elements of page from HTML code
    b) Creation of dixtionary that describes opinions structure with selectors for particularopinion elements
    c) Using dictionary comprehension to extract all opinions elements on the basis of opinions structure dictionary
6) Adjustment of data types from diffrent opinions
7) Translation of certain opinions elements into english
