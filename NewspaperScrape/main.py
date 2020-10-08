# Imports all the methods and variables from each script.
from news_extract import *
from news_scrape import *
from news_nlp import *
import time

# Welcome Messages and Introduction
print("Welcome to the Newspaper Scrape Project. \nIn seconds, you will have access to the latest articles "
      "in the technology section of the New York Times. \nIn addition, you will also be able to know whether the "
      "article is positive or negative and the extent of the writer's bias.")
print()

# Getting the user input; adding an element of personalization!
name = input("Enter your name to get started: ")

# Console Display
print("Welcome " + name + "! \nYou will now see the latest technology articles in the New York Times...")
print("Extracting article hyperlinks...")
time.sleep(2)
print("Retrieving summaries...")
print()
time.sleep(2)

# Gets all the latest URL's from the NY Times Technology Section. (see news_extract.py for more detail)
content_string = get_content_string(my_url)
starts, ends = findOccurrences(content_string)
url_list = get_all_urls(starts, ends, content_string)

# Gets the article summary and performs sentiment analysis on the chosen URL.
# For more information on how this works, visit news_scrape.py and news_nlp.py!
for url in url_list:
    print("Article URL: " + str(url))
    article_summary = summarize_article(url)
    find_sentiment(article_summary)
    print("------------------------------------------------")
    time.sleep(7)  # Allows user to get through all the text.

# Closing Messages
print()
print("The articles have been successfully extracted!")
print("In total, we were able to extract " + str(len(url_list)) + " different articles!")
print("Thanks for participating, " + name + "!")
