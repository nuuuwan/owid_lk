from owid_lk._constants import LK_CONTS_WORLD, LK_NAME


def covid19_deaths(data_list):
    lk_data_list = list(
        filter(
            lambda d: d['location'] == LK_NAME,
            data_list,
        )
    )
    latest_lk_data = lk_data_list[-1]
    lk_day = latest_lk_data['date']

    entity_to_value = {}
    for entity in LK_CONTS_WORLD:
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
