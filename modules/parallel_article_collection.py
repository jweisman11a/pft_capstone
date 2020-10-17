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
from scrape_pft_comments import scrape_comments_from_pft_article


if __name__ == '__main__':

    # Check python, platform and # of cores available
    # https://sedeh.github.io/python-pandas-multiprocessing-workaround.html
    if False:
        print(sys.version)
        print(platform.platform())
        print(f"CPU cores: {multiprocessing.cpu_count()}")
        print('-' * 50)

    # Serial article collection
    if False:
        start_time = time.time()
        print('Begin serial article collection...')

        for page in tqdm(range(1,25)):
            url = f'https://profootballtalk.nbcsports.com/category/rumor-mill/page/{str(page)}/'
            article_page = scrape_pft_rumormill(url)
            header = False if os.path.exists(f'../data/serial_article_test.csv') else True
            article_page.to_csv(f'../data/serial_article_test.csv', header=header, index=False, mode='a')

        print(f'--- {time.time() - start_time} seconds ---')

    # Parallel article collection
    if True:
        start_time = time.time()
        print('Begin parallel article collection...')

        last_page = 100
        urls = [f'https://profootballtalk.nbcsports.com/category/rumor-mill/page/{str(i)}/' for i in range(1,last_page)]
        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            results = list(tqdm(pool.imap(scrape_pft_rumormill, urls), total=last_page))

        results_df = pd.concat(results)
        results_df.to_csv(f'../data/parallel_article_test_2.csv', header=True, index=False, mode='a')

        print(f'--- {time.time() - start_time} seconds ---')
