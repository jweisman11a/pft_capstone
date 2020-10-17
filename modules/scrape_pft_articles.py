# Load libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime as dt


def scrape_pft_rumormill(url='https://profootballtalk.nbcsports.com/category/rumor-mill/page/1/'):
    """Function scrapes articles from PFT's rumor mill page

    Notes:
        Expect URL to be in this format:
            https://profootballtalk.nbcsports.com/category/rumor-mill/page/{page_number}/

        Page numbers start at 1
        There are 15 articles/page
        Not all articles have comments enabled

        Function captures the following elements of the passed article URL:
            URL
            Title
            Author
            Post Date
            Text of the article
            # of Comments (or whether comments were disabled)
        Function add a datetime stamp indicating when it was scraped

        Data returned is raw // not processed by this function

    Args:
        url (str): The URL of the PFT Rumor Mill page to be scraped
    Returns:
        A pandas DataFrame containing the elements outlined above
    """

    # Sent GET request to URL and convert response to HTML soup
    r = requests.get(url)
    assert r.status_code == 200, 'Unexpected response from request'
    scrape_time = dt.datetime.now()
    soup = BeautifulSoup(r.text, 'html.parser')

    # Get the article's title and URL
    articles = soup.findAll('h1', {"class":"entry-title"})
    if len(articles) != 15:
        message = f"""
                    When scraping URL: {url}
                    Only {len(articles)} articles were found.
                    This function expects 15 articles to be returned.
                    Please confirm you passed in a URL in the expected format.
                    Example: https://profootballtalk.nbcsports.com/category/rumor-mill/page/<page_number>/
                    """
        raise Exception(message)
    article_titles = [a.text for a in articles]
    article_links = [a.find('a').get('href') for a in articles]

    # Get the article's published date
    published_dates = soup.findAll('span', {"class":"entry-date published"})
    article_publish_dates = [d.text for d in published_dates]

    # Get the article's author
    authors = soup.findAll('span', {"class":"byline"})
    article_authors = [a.text for a in authors]

    # Get the article's # of comments
    comments = soup.findAll('span', {"class":"post-footer-link"})
    article_comment_count = [c.text for c in comments if c.find('a').get('href').endswith('#respond') or c.find('a').get('href').endswith('#comments')]

    # If less than 15 results above, determine which articles have comments disabled
    if len(article_comment_count) != 15:
        # print('Less than 15 comment links found. Using alternative collection method.')
        article_comment_count = list()
        all_articles = soup.findAll('article', {'class':"content-item"})
        for art in all_articles:
            all_links = art.find_all('a')
            counter = 0
            for link in all_links:
                if link.get('href').endswith('#respond') or link.get('href').endswith('#comments'):
                    article_comment_count.append(link.text)
                    counter += 1
            if counter == 0:
                article_comment_count.append('Comments Disabled')

    # Get the article's content
    articles_body = soup.findAll('div', {"class":"entry-content"})
    article_content = [b.text for b in articles_body]

    # Compile results and convert into a DataFrame
    page_data = list(zip(article_titles, article_links, article_publish_dates, article_authors,
                         article_content, [scrape_time for _ in range(len(article_titles))],
                        [url for _ in range(len(article_titles))]))
    return pd.DataFrame(page_data, columns=['article_title','article_url','article_post_date','article_author',
                                            'article_body','scrape_datetime', 'page_url'])
