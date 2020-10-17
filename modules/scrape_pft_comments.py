# Load libraries
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime as dt



def scrape_comments_from_pft_article(url='https://profootballtalk.nbcsports.com/2020/10/03/eagles-add-five-from-practice-squad-ahead-of-sundays-game/'):
    """Function scrapes comments from a single article on PFT

    Notes:
        Expect URL to be in this format:
            https://profootballtalk.nbcsports.com/YYYY/MM/DD/{article-title}/

        selenium:
            Using Chrome webdriver
            Chrome version 86.0.4240.75 (Official Build) (64-bit)
            https://sites.google.com/a/chromium.org/chromedriver/downloads

        Function captures the following elements of each article:
            Username
            Post datetime
            Text of the comment
            # of likes and dislikes
        Function add a datetime stamp indicating when it was scraped

    Args:
        url (str): The URL of the PFT article to be scraped
    Returns:
        A pandas DataFrame
    """

    # Use headless driver to force JS elements in comments to load
    chrome_options = Options()
    chrome_options.headless = True
    driver = webdriver.Chrome(executable_path='./assets/chromedriver.exe', options=chrome_options)
    driver.get(url)
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, features="html.parser")
    scrape_time = dt.datetime.now()

    # Get the names of the commentors on the article
    article_commenters = soup.findAll('b', {"class":"fn"})
    commentors = [c.text for c in article_commenters]

    # Get the dates of the comments from the article
    article_times = soup.findAll('div', {"class":"comment-metadata"})
    times = [t.text.strip() for t in article_times]

    # Get the message of the comment
    article_comments = soup.findAll('div', {"class":"comment-content"})
    comments = [c.text for c in article_comments]

    # Get comment likes and dislikes
    likes_and_dislikes = soup.findAll('div', {"class":"rating-nero-value"})
    likes_and_dislikes = [t.text for t in likes_and_dislikes]
    likes, dislikes = likes_and_dislikes[::2], likes_and_dislikes[1::2]

     # Compile results
    comment_page = list(zip([url for _ in range(len(commentors))], commentors, times,
                            comments, likes, dislikes, [dt.datetime.now() for _ in range(len(commentors))]))

    return pd.DataFrame(comment_page, columns=['article_url','commentor','comment_datetime',
                                               'comment_body','likes','dislikes','scrape_datetime'])
