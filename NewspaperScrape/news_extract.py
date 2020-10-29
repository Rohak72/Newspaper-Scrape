# Description: This script extracts ALL the latest articles from the technology section of the New York Times with
# BeautifulSoup.

import requests
from bs4 import BeautifulSoup as soup

my_url = "https://www.nytimes.com/section/technology"


# Method Purpose: This method extracts a content dictionary from an HTML outline of the NY Times Tech Section.
# Parameter: The URL of the NY Times Tech Section.
# Steps (How it Works):
# 1. Gets a script of all the HTML on the page.
# 2. Gets an article list - a snippet of the HTML outline including all of the articles.
# 3. The content string is the first element of this list.
# 4. The index of the "itemListElement" is used to extract a library of all the article hyperlinks and metadata.
# 5. A substring of the content string is taken to remove the "itemListElement" from the string.

def get_content_string(url):
    page = requests.get(url)
    page_soup = soup(page.content, 'html.parser')
    # Use the below statement as a visualizer of the HTML outline.
    # print(page_soup)
    containers = page_soup.find_all("script", {"type": "application/ld+json"})

    article_list = []
    for container in containers:
        for dictionary in container:
            article_list.append(dictionary)
    article_list[0:2] = [''.join(article_list[0:2])]
    content_string = article_list[0]
    article_index = content_string.index("itemListElement")
    content_string = content_string[article_index + 18:]
    return content_string


# Method Purpose: Finds the start and end of all correct article hyperlinks in the previously extracted content string.
# Parameter: The content string pulled from the NY Times Tech Section HTML outline.
# Steps (How it Works):
# 1. A list comprehension methodology searches for the common hyperlink beginning across all articles.
# 2. A list comprehension methodology searches for the common ".html" extension at the end of each article hyperlink.
# 3. Each element of the end_indices list are incremented by 5 in order to get the last character of the hyperlink.
# 4. Validation techniques are used to equalize the lengths of the start and end indices.

def findOccurrences(content_string):
    start_indices = [i for i in range(len(content_string)) if
                     content_string.startswith('https://www.nytimes.com/2020', i)]
    end_indices = [i for i in range(len(content_string)) if content_string.startswith('.html', i)]
    end_indices = [x + 5 for x in end_indices]

    if len(start_indices) > len(end_indices):
        difference = len(start_indices) - len(end_indices)
        start_indices = start_indices[:difference]
    if len(end_indices) > len(start_indices):
        difference = len(end_indices) - (len(end_indices) - len(start_indices))
        end_indices = end_indices[:difference]
    return start_indices, end_indices


# Method Purpose: Extracts all article hyperlinks from the content string.
# Parameters: The starting and ending indices of the hyperlinks in the content string.
# Steps (How it Works):
# 1. Defines an empty url_list which will be used for the aggregation of the URL's themselves.
# 2. Uses a for-range loop to get all the indices of start_indices list.
# Side Note: Since the lists are EQUALIZED in length from the previous method, the lengths of both will be equal.
# 3. Gets a substring from the content string with the starting and ending index of the hyperlink.
# 4. The hyperlinks are added to the url_list defined in Step 1.

def get_all_urls(start_indices, end_indices, content_string):
    url_list = []
    for i in range(len(start_indices)):
        url_list.append(content_string[start_indices[i]:end_indices[i]])
    return url_list
