import os
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from owid_lk._utils import (get_data_dir, get_data_file, get_image_file,
                            get_url, log)

TIME_LOAD = 2
TIME_WAIT_DEFAULT = 2
TIME_WAIT_DOWNLOAD = 2
TIME_COMPLETE_DOWNLOAD = 10
TIME_COMPLETE_DOWNLOAD_LONG = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 3200, 1800


def get_firefox_profile():
    data_dir = get_data_dir()
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference(
        "browser.download.dir",
        data_dir,
    )
    profile.set_preference(
        "browser.helperApps.neverAsk.saveToDisk", "image/png; text/csv; "
    )
    return profile


def get_firefox_options():
    options = Options()
    options.headless = True
    return options


def scrape(d):
    url = get_url(d)

    log.info(f'Scraping {url}...')

    driver = webdriver.Firefox(
        options=get_firefox_options(), firefox_profile=get_firefox_profile()
    )
    driver.get(url)
    time.sleep(TIME_LOAD)
    driver.set_window_size(SCREEN_WIDTH, SCREEN_HEIGHT)

    a_cookies = driver.find_element("xpath", '//button[text()="I agree"]')
    a_cookies.click()
    time.sleep(TIME_WAIT_DEFAULT)

    a_download = driver.find_element("xpath", '//a[text()=" Download"]')
    a_download.click()
    time.sleep(TIME_WAIT_DOWNLOAD)

    # Downloadin image...

    button_download_png = driver.find_element(
        "xpath", '//button[@data-track-note="chart-download-png"]'
    )
    button_download_png.click()
    log.info('Downloading image...')
    time.sleep(TIME_COMPLETE_DOWNLOAD)

    down_image_file = d.get('down_image_file', None)
    data_dir = get_data_dir()
    if down_image_file:
        image_file = get_image_file(d)
        os.system(f'mv "{data_dir}/{down_image_file}" "{image_file}"')

    # Downloadin data...

    func_get_tweet_text = d.get('func_get_tweet_text', None)
    if func_get_tweet_text:
        down_data_file = d.get('down_data_file', None)
        data_file = get_data_file(d)

        if not down_data_file or not os.path.exists(data_file):
            button_download_csv = driver.find_element(
                "xpath", '//button[@data-track-note="chart-download-csv"]'
            )
            button_download_csv.click()
            log.info('Downloading data...')
            time.sleep(TIME_COMPLETE_DOWNLOAD_LONG)

            if down_data_file:
                data_file = get_data_file(d)
                os.system(f'mv "{data_dir}/{down_data_file}" "{data_file}"')

    driver.quit()

    log.info(f'Done. Saved data to {data_dir}')
