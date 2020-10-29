# Load libraries
import sys
import os
import platform
import time
import pandas as pd
import multiprocessing
from tqdm import tqdm


# Load modules
from scrape_pft_articles import scrape_pft_rumormill
from scrape_pft_comments import scrape_comments_from_pft_article_v2


def load_article_urls(data, article_url_column_name):
    ''' Create list of article urls '''
    articles = pd.read_csv(data, usecols=[article_url_column_name], header=0)
    return articles[article_url_column_name].tolist()


if __name__ == '__main__':

    # Serial comment collection
    if False:
        article_data = '../data/raw/pft_articles_collected_w_comment_counts_20201025.csv'
        urls = load_article_urls(article_data, 'article_url')

        start_time = time.time()
        print(f'Begin comment collection on {len(urls)} articles...')

        results = list()
        for url in tqdm(urls[0:100]):
            comments = scrape_comments_from_pft_article_v2(url)
            results.append(comments)

        if len(results) > 0:

            results_df = pd.concat(results)
            results_df.to_csv(f'../data/raw/pft_comments_collected_20201027_test.csv', header=True, index=False, mode='a')
        else:
            print('No comments were found.')

        print(f'--- {time.time() - start_time} seconds ---')


    # Parallel comment collection
    if True:
        article_data = '../data/raw/pft_articles_collected_w_comment_counts_20201025.csv'
        urls = load_article_urls(article_data, 'article_url')

        start_time = time.time()
        urls = urls[200000:]
        print(f'Begin comment collection on {len(urls)} articles...')

        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            results = list(tqdm(pool.imap(scrape_comments_from_pft_article_v2, urls), total=len(urls)))

        if len(results) > 0:
            results_df = pd.concat(results)
            results_df.to_csv(f'../data/raw/pft_comments_collected_20201028.csv', header=True, index=False, mode='a')
        else:
            print('No comments were found.')

        print(f'--- {time.time() - start_time} seconds ---')
