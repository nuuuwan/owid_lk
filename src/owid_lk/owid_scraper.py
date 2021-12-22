import time

import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from utils import timex

from owid_lk._utils import log

TIME_LOAD = 0.5
TIME_WAIT_DEFAULT = 0.5
TIME_WAIT_DOWNLOAD = 2
SCREEN_WIDTH, SCREEN_HEIGHT = 3200, 1800


def get_data_dir():
    date_id = timex.get_date_id()
    return f'/tmp/owid_lk.{date_id}'


def init():
    data_dir = get_data_dir()
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)


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


def scrape(url):

    log.info(f'Scraping {url}...')

    driver = webdriver.Firefox(
        options=get_firefox_options(), firefox_profile=get_firefox_profile()
    )
    driver.get(url)
    time.sleep(TIME_LOAD)
    driver.set_window_size(SCREEN_WIDTH, SCREEN_HEIGHT)

    a_cookies = driver.find_element_by_xpath('//button[text()="I agree"]')
    a_cookies.click()
    time.sleep(TIME_WAIT_DEFAULT)

    a_download = driver.find_element_by_xpath('//a[text()=" Download"]')
    a_download.click()
    time.sleep(TIME_WAIT_DOWNLOAD)

    button_download_png = driver.find_element_by_xpath(
        '//button[@data-track-note="chart-download-png"]'
    )
    button_download_png.click()
    time.sleep(TIME_WAIT_DOWNLOAD)

    button_download_png = driver.find_element_by_xpath(
        '//button[@data-track-note="chart-download-csv"]'
    )
    button_download_png.click()
    time.sleep(TIME_WAIT_DOWNLOAD)

    driver.quit()

    data_dir = get_data_dir()
    log.info(f'Saved data to {data_dir}')
