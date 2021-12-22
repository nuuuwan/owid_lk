import os
import urllib

from owid_lk import owid_scraper
from owid_lk.CONFIG import CONFIG

URL_BASE = 'https://ourworldindata.org/grapher'

if __name__ == '__main__':
    owid_scraper.init()

    for d in CONFIG:
        url = os.path.join(
            URL_BASE, d['name'] + '?' + urllib.parse.urlencode(d['url_params'])
        )
        owid_scraper.scrape(url)
