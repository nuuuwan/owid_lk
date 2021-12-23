"""Constants."""
import os

CACHE_NAME = 'owid_lk'
CACHE_TIMEOUT = 3600

URL_OWID = 'https://ourworldindata.org'
URL_GRAPHER = os.path.join(URL_OWID, 'grapher')
URL_EXPLORERS = os.path.join(URL_OWID, 'explorers')


def join_tilde(*_list):
    return '~'.join(_list)


LK_NAME = 'Sri Lanka'
LK_CONTS_WORLD_URL = join_tilde(
    'Africa',
    'Asia',
    'European Union',
    'LKA',
    'North America',
    'Oceania',
    'OWID_WRL',
    'South America',
)

LK_CONTS_WORLD_NAMES = [
    'Africa',
    'Asia',
    'European Union',
    'North America',
    'Oceania',
    'South America',
    'Sri Lanka',
    'World',
]
