import os
import urllib

from owid_lk import owid_scraper, tweeter
from owid_lk._utils import get_url, init
from owid_lk.CONFIG import CONFIG



if __name__ == '__main__':
    # init()

    for d in CONFIG:
        url = get_url(d)
        owid_scraper.scrape(url)
        tweeter.tweet(d)
