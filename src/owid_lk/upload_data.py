import os
import urllib

from owid_lk import _utils, owid_scraper, tweeter
from owid_lk.CONFIG import CONFIG

URL_BASE = 'https://ourworldindata.org/grapher'

if __name__ == '__main__':
    # _utils.init()

    for d in CONFIG:
        url = os.path.join(
            URL_BASE, d['name'] + '?' + urllib.parse.urlencode(d['url_params'])
        )
        owid_scraper.scrape(url)
        tweeter.tweet(d)
