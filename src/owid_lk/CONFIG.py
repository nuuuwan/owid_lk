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


CONFIG = [
    dict(
        name='covid-vaccine-booster-doses-per-capita',
        url_params=dict(
            time='2021-08-21..latest',
            country='OWID_WRL~LKA~Asia~Africa~South America'
            + '~European Union~North America~Oceania',
        ),
        func_get_tweet_text=_covid_vaccine_booster_doses_per_capita,
    )
]
