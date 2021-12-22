"""Utils."""

import logging
import os
import urllib

from utils import timex

URL_BASE = 'https://ourworldindata.org/grapher'

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('owid_lk')


def get_data_dir():
    date_id = timex.get_date_id()
    return f'/tmp/owid_lk.{date_id}'


def init():
    data_dir = get_data_dir()
    os.system(f'rm -rf {data_dir}')
    os.system(f'mkdir {data_dir}')


def get_url(d):
    return os.path.join(
        URL_BASE, d['name'] + '?' + urllib.parse.urlencode(d['url_params'])
    )
