def _covid_vaccine_booster_doses_per_capita(data_list):
    lk_data_list = list(
        filter(
            lambda d: d['Entity'] == 'Sri Lanka',
            data_list,
        )
    )
    latest_lk_data = lk_data_list[-1]
    lk_day = latest_lk_data['Day']

    entity_to_value = {}
    for entity in [
        'Africa',
        'Asia',
        'European Union',
        'North America',
        'Oceania',
        'South America',
        'Sri Lanka',
    ]:
        entity_data_list = list(
            filter(
                lambda d: d['Entity'] == entity and d['Day'] == lk_day,
                data_list,
            )
        )
        if entity_data_list:
            entity_data = entity_data_list[0]
            entity_value = (float)(entity_data['total_boosters_per_hundred'])
            entity_to_value[entity] = entity_value

    sorted_entity_and_value = sorted(
        entity_to_value.items(), key=lambda x: -x[1]
    )

    entity_info_list = '\n'.join(
        list(
            map(
                lambda x: '%4.2f #%s' % (x[1], x[0].replace(' ', '')),
                sorted_entity_and_value,
            )
        )
    )

    return f'''Boosters per 100 people ({lk_day})

{entity_info_list}'''


def _covid19_deaths(data_list):
    lk_data_list = list(
        filter(
            lambda d: d['location'] == 'Sri Lanka',
            data_list,
        )
    )
    latest_lk_data = lk_data_list[-1]
    lk_day = latest_lk_data['date']

    entity_to_value = {}
    for entity in [
        'Africa',
        'Asia',
        'European Union',
        'North America',
        'Oceania',
        'South America',
        'Sri Lanka',
    ]:
        entity_data_list = list(
            filter(
                lambda d: d['location'] == entity and d['date'] == lk_day,
                data_list,
            )
        )
        if entity_data_list:
            entity_data = entity_data_list[0]
            entity_value = (float)(
                entity_data['new_deaths_smoothed_per_million']
            )
            entity_to_value[entity] = entity_value

    sorted_entity_and_value = sorted(
        entity_to_value.items(), key=lambda x: -x[1]
    )

    entity_info_list = '\n'.join(
        list(
            map(
                lambda x: '%4.2f #%s' % (x[1], x[0].replace(' ', '')),
                sorted_entity_and_value,
            )
        )
    )

    return f'''Daily New Deaths per 1M people - 7day avg. ({lk_day})

{entity_info_list}'''


CONFIG = [
    dict(
        name='covid-vaccine-booster-doses-per-capita',
        url_params=dict(
            time='2021-08-21..latest',
            country='OWID_WRL~LKA~Asia~Africa~South America'
            + '~European Union~North America~Oceania',
        ),
        func_get_tweet_text=_covid_vaccine_booster_doses_per_capita,
    ),
    dict(
        name='covid19-deaths',
        url='https://ourworldindata.org/explorers/coronavirus-data-explorer?zoomToSelection=true&time=2020-03-01..latest&facet=none&pickerSort=desc&pickerMetric=new_deaths_per_million&Metric=Confirmed+deaths&Interval=7-day+rolling+average&Relative+to+Population=true&Align+outbreaks=false&country=LKA~Asia~North+America~South+America~European+Union~Africa~Oceania~OWID_WRL',
        down_image_file='coronavirus-data-explorer.png',
        down_data_file='owid-covid-data.csv',
        func_get_tweet_text=_covid19_deaths,
    ),
]
