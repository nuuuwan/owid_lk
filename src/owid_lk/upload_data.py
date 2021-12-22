from owid_lk import owid_scraper

if __name__ == '__main__':
    owid_scraper.init()
    TEST_URL = 'https://ourworldindata.org/grapher/covid-vaccine-booster-doses-per-capita?time=2021-08-21..latest&country=OWID_WRL~LKA~Asia~Africa~South+America~European+Union~North+America~Oceania'
    owid_scraper.scrape(TEST_URL)
