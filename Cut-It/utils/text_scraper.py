"""
    - This is the logic behind the scraper for webpage text
    - It works on the listed websites and YouTube (via Captions)
    - This can never (and will never) work on Paywalled sites due to legal issues
    TODO: implement 1 class with YouTube and Newspaper3k support (https://github.com/codelucas/newspaper)
"""

import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi

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
    - YouTube Captions
    + others
"""

class text:

    @staticmethod

    def scrape(URL):
        text = ""

        # Using YouTube API if applicable (https://github.com/jdepoix/youtube-transcript-api)
        if "youtube.com" in URL:

            VIDEO_ID = URL.replace('https://www.youtube.com/watch?v=', '')
            data = YouTubeTranscriptApi.get_transcript(video_id=VIDEO_ID)
            for timestamp in data: # Data returned has other things not needed (eg. timestamp)
                text += timestamp["text"] + " "
            return text[:-1]

        # If the URL was a video, a val would've been returned, so we can assume it's a URL
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, 'html.parser')

        # Defining site rules & filtering with conditionals
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