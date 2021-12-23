from owid_lk._constants import LK_CONTS_WORLD, URL_EXPLORERS, URL_GRAPHER
from owid_lk.custom.covid19_deaths import covid19_deaths
from owid_lk.custom.covid_vaccine_booster_doses_per_capita import \
    covid_vaccine_booster_doses_per_capita

CONFIG = [
    dict(
        name='covid-vaccine-booster-doses-per-capita',
        url_base=URL_GRAPHER,
        url_params=dict(
            time='2021-08-21..latest',
            country=LK_CONTS_WORLD,
        ),
        func_get_tweet_text=covid_vaccine_booster_doses_per_capita,
    ),
    dict(
        name='covid19-deaths',
        url_base=URL_EXPLORERS,
        url_data='coronavirus-data-explorer',
        url_params=dict(
            time='2020-03-01..latest',
            pickerMetric='new_deaths_per_million',
            Metric='Confirmed deaths',
            Interval='7-day+rolling+average',
            country=LK_CONTS_WORLD,
        ),
        down_image_file='coronavirus-data-explorer.png',
        down_data_file='owid-covid-data.csv',
        func_get_tweet_text=covid19_deaths,
    ),
]
