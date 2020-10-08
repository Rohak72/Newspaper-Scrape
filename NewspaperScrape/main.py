# Mark directory as sources root first
from news_extract import *
from news_scrape import *
from news_nlp import *
import time

print("Welcome to the Newspaper Scrape Project. \nIn seconds, you will have access to the latest articles "
      "in the technology section of the New York Times. \nIn addition, you will also be able to know whether the "
      "article is positive or negative and the extent of the writer's bias.")
print()
name = input("Enter your name to get started: ")
print("Welcome " + name + "! \nYou will now see the latest technology articles in the New York Times...")
print("Extracting article hyperlinks...")
time.sleep(2)
print("Retrieving summaries...")
print()
time.sleep(2)
content_string = get_content_string(my_url)
starts, ends = findOccurrences(content_string)
url_list = get_all_urls(starts, ends, content_string)
for url in url_list:
    print("Article URL: " + str(url))
    article_summary = summarize_article(url)
    find_sentiment(article_summary)
    print("------------------------------------------------")
    time.sleep(7)

print()
print("The articles have been successfully extracted!")
print("In total, we were able to extract " + str(len(url_list)) + " different articles!")
print("Thanks for participating, " + name + "!")