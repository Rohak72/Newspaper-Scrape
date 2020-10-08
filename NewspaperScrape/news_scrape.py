# Description: This program scrapes and summarizes news articles from the New York Times.

from newspaper import Article

# The following URLs need to be emailed to rohakjain@gmail.com
# https://www.nytimes.com/2020/09/22/technology/digital-divide-solutions.html
# https://www.nytimes.com/2020/10/05/technology/how-did-ransomware-get-so-bad.html


def summarize_article(url):
    article = Article(url)

    article.download()
    article.parse()
    # Punkt is a sentence tokenizer which is useful for extracting and detecting text.
    article.download('punkt')
    article.nlp()

    # DO the below line FIRST before doing the loop!
    # print("Author: " + str(article.authors))

    # Get the author or authors of the article
    author_string = "Author(s): "
    for author in article.authors:
        author_string += author  # adds all authors (if more than 1) to the author string.
    print(author_string)

    # DO the following TWO lines before doing the modification!
    # print("Publish Date: " + str(article.publish_date))
    # print("Publish Date: " + str(type(article.publish_date)))

    # Get the publish date of the article
    date = article.publish_date
    # strftime() converts a tuple or struct_time representing a time to a string as specified by the format argument.
    # Here, it is used to mark the month, day, and year of the date in a readable format.
    print("Publish Date: " + str(date.strftime("%m/%d/%Y")))

    # Get the top image of the article
    print("Top Image Url: " + str(article.top_image))

    # Do the below line FIRST before doing the loop!
    # print(article.images)

    # Get the article images
    image_string = "All Images: "
    for image in article.images:
        image_string += "\n\t" + image  # adds a newline and a tab before each image is printed
    print(image_string)
    print()

    # Get the article summary
    print("A Quick Article Summary")
    print("----------------------------------------")
    print(article.summary)

    return article.summary
