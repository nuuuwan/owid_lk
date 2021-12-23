from utils.dt import parse_float

from owid_lk._constants import LK_CONTS_WORLD_NAMES, LK_NAME


def _coronavirus_data_explorer(data_list, value_key_field, title):
    lk_data_list = list(
        filter(
            lambda d: d['location'] == LK_NAME,
            data_list,
        )
    )
    latest_lk_data = lk_data_list[-1]
    lk_day = latest_lk_data['date']

    entity_to_value = {}
    for entity in LK_CONTS_WORLD_NAMES:
        entity_data_list = list(
            filter(
                lambda d: d['location'] == entity and d['date'] == lk_day,
                data_list,
            )
        )
        if entity_data_list:
            entity_data = entity_data_list[0]
            entity_value = parse_float(entity_data[value_key_field], 0)
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

    return f'''{title} ({lk_day})

{entity_info_list}'''


def _coronavirus_data_explorer_factory(value_key_field, title):
    def _f(data_list):
        return _coronavirus_data_explorer(data_list, value_key_field, title)

    return _f
