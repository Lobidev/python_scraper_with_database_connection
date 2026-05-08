from bs4 import BeautifulSoup
import requests

url = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(url.text, "html.parser")

class Quote:
    def __init__(self, id, author, text, tags):
        self.id     = id
        self.author = author
        self.text   = text
        self.tags   = tags

    def __repr__(self):
        return f"Quote(id={self.id}, author='{self.author}', text='{self.text[:30]}...', tags={self.tags})"


def data():
    authors_html = soup.findAll('small', class_="author")
    texts_html   = soup.findAll('span',  class_="text")
    quotes_html  = soup.findAll('div',   class_="quote")

    quotes = []

    for i, quote_block in enumerate(quotes_html):
        author = authors_html[i].text
        text   = texts_html[i].text
        tags   = [tag.text for tag in quote_block.findAll('a', class_="tag")]

        quote = Quote(
            id     = i + 1,
            author = author,
            text   = text,
            tags   = tags
        )
        quotes.append(quote)

    return quotes



# Für die Datenbank konvertiert
def quote_datas():
    quotes = data()
    return [(
        q.id,
        q.author,
        q.text,
        ", ".join(q.tags)  # ['change', 'deep-thoughts'] → "change, deep-thoughts"
    ) for q in quotes]