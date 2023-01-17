"""Utils."""

import logging
import os
import urllib

from utils import TIME_FORMAT_DATE_ID, Time

from owid_lk._constants import URL_GRAPHER

URL_BASE = 'https://ourworldindata.org/grapher'

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('owid_lk')


def get_data_dir():
    date_id = TIME_FORMAT_DATE_ID.stringify(Time())
    return f'/tmp/owid_lk.{date_id}'


def get_image_file(d):
    return os.path.join(get_data_dir(), d['name'] + '.png')


def get_data_file(d):
    return os.path.join(get_data_dir(), d['name'] + '.csv')


def init():
    data_dir = get_data_dir()
    log.info(f'Cleaning {data_dir}...')
    os.system(f'rm -rf {data_dir}')
    os.system(f'mkdir {data_dir}')


def get_url(d):
    url_base = d['url_base']
    url_params = d['url_params']
    if url_base == URL_GRAPHER:
        url_data = d['name']
    else:
        url_data = d.get('url_data')

    url = os.path.join(
        url_base, url_data + '?' + urllib.parse.urlencode(url_params)
    )
    return url
