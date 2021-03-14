import requests
from bs4 import BeautifulSoup
from resources.newzpaper import Article

# Text class depreciated
"""
Supported Websites (Text Class):
    - AP News
    - CNN
    - Fox
    - Brookings
    - Reuters
    - CSIS
    - Forbes
    - ABC News
    - CBS News
    - CNET 
    - NY Times
    - NBC News
    - USA Today
"""
class text:

    @staticmethod
    def get(URL):
        text = ""

        r = requests.get(URL)
        soup = BeautifulSoup(r.text, 'html.parser')

        if "cnn.com" in URL:
            paragraphs = soup.find_all('div', class_="l-container")
        
        elif "foxnews.com" in URL:
            raw_paragraphs = soup.find_all('div')
            paragraphs = []
            for paragraph in raw_paragraphs:
                if paragraph.has_attr('class'):
                    if paragraph['class'][0] == 'article-content':
                        paragraphs.append(paragraph) 
        
        elif "nytimes.com" in URL:
            raw_paragraphs = soup.find_all('section')
            paragraphs = []
            for paragraph in raw_paragraphs:
                if paragraph.has_attr('name'):
                    paragraphs.append(paragraph)
        
        elif "nbcnews.com" in URL:
            raw_paragraphs = soup.find_all('div')
            paragraphs = []
            for paragraph in raw_paragraphs:
                if paragraph.has_attr('class') and 'article-body__content' in paragraph['class']:
                    paragraphs.append(paragraph) 
        else:
            paragraphs = soup.find_all('p')

        for paragraph in paragraphs:
            text += paragraph.get_text()

        return text

class news:
    @staticmethod
    def paper(URL):
        article = Article(URL)
        article.download()
        article.parse()
        return article.text