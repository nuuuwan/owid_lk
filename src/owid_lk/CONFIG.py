from utils import timex

from owid_lk._constants import LK_CONTS_WORLD_URL, URL_EXPLORERS, URL_GRAPHER
from owid_lk.custom._coronavirus_data_explorer import \
    _coronavirus_data_explorer_factory
from owid_lk.custom.covid_vaccine_booster_doses_per_capita import \
    covid_vaccine_booster_doses_per_capita


def get_time_for_window(dt):
    date_start = timex.get_date(timex.get_unixtime() - dt)
    return f'{date_start}..latest'


WINDOW_26WEEKS = get_time_for_window(timex.SECONDS_IN.WEEK * 26)
WINDOW_52WEEKS = get_time_for_window(timex.SECONDS_IN.WEEK * 52)
TAB_MAP = 'map'

COVID_EXPLORER_DEFAULTS = dict(
    url_base=URL_EXPLORERS,
    url_data='coronavirus-data-explorer',
    url_params=dict(
        time=WINDOW_26WEEKS,
        pickerMetric='new_deaths_per_million',
        Metric='Confirmed deaths',
        Interval='7-day+rolling+average',
        country=LK_CONTS_WORLD_URL,
    ),
    down_image_file='coronavirus-data-explorer.png',
    down_data_file='owid-covid-data.csv',
)

CONFIG = [
    dict(
        name='covid-vaccine-booster-doses-per-capita',
        url_base=URL_GRAPHER,
        url_params=dict(
            time=WINDOW_26WEEKS,
            country=LK_CONTS_WORLD_URL,
        ),
        func_get_tweet_text=covid_vaccine_booster_doses_per_capita,
    ),
    COVID_EXPLORER_DEFAULTS
    | dict(
        name='covid19-deaths',
        url_params=dict(
            tab=TAB_MAP,
            time=WINDOW_26WEEKS,
            Metric='Confirmed deaths',
            Interval='7-day+rolling+average',
            country=LK_CONTS_WORLD_URL,
        ),
        func_get_tweet_text=_coronavirus_data_explorer_factory(
            'new_deaths_smoothed_per_million',
            'Daily New Deaths per 1M people - 7day avg.',
        ),
    ),
    COVID_EXPLORER_DEFAULTS
    | dict(
        name='covid19-reproduction-rate',
        url_params=dict(
            time=WINDOW_52WEEKS,
            Metric='Reproduction rate',
            Interval='7-day+rolling+average',
            country=LK_CONTS_WORLD_URL,
        ),
    ),
    COVID_EXPLORER_DEFAULTS
    | dict(
        name='covid19-case-fatality-rate',
        url_params=dict(
            time=WINDOW_26WEEKS,
            Metric='Case fatality rate',
            Interval='7-day+rolling+average',
            country=LK_CONTS_WORLD_URL,
        ),
    ),
    COVID_EXPLORER_DEFAULTS
    | dict(
        name='covid19-omicron-variant',
        url_params=dict(
            time=WINDOW_26WEEKS,
            Metric='Omicron variant',
            Interval='7-day+rolling+average',
            country=LK_CONTS_WORLD_URL,
        ),
    ),
    COVID_EXPLORER_DEFAULTS
    | dict(
        name='covid19-tests',
        url_params=dict(
            time=WINDOW_26WEEKS,
            Metric='Tests',
            Interval='7-day+rolling+average',
            country=LK_CONTS_WORLD_URL,
        ),
        func_get_tweet_text=_coronavirus_data_explorer_factory(
            'new_tests_smoothed_per_thousand',
            'Daily New Tests per 1K people - 7day avg.',
        ),
    ),
]
