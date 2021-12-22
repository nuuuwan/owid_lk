from owid_lk._utils import log

def scrape(url):
    log.info(f'Scraping {url}...')
    pass


if __name__ == '__main__':
    TEST_URL = 'https://ourworldindata.org/grapher/covid-vaccine-booster-doses-per-capita?time=2021-08-21..latest&country=OWID_WRL~LKA~Asia~Africa~South+America~European+Union~North+America~Oceania'

    scrape(TEST_URL)
