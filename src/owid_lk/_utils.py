"""Utils."""

import logging
import os

from utils import timex

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('owid_lk')


def get_data_dir():
    date_id = timex.get_date_id()
    return f'/tmp/owid_lk.{date_id}'


def init():
    data_dir = get_data_dir()
    os.system(f'rm -rf {data_dir}')
    os.system(f'mkdir {data_dir}')
