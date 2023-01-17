import random
import time

from utils import TIME_FORMAT_TIME, File, Time

from owid_lk import owid_scraper, tweeter
from owid_lk._utils import init, log
from owid_lk.CONFIG import CONFIG


def write_readme(info_list):
    readme_file = '/tmp/README.md'
    time_str = TIME_FORMAT_TIME.stringify(Time())

    valid_info_list = list(map(lambda x: x, info_list))
    rendered_info_list = list(
        map(
            lambda info: '* %s' % (info['name']),
            valid_info_list,
        )
    )
    content = '\n\n'.join(
        [
            '# Our World in Data (Sri Lanka)',
            f'*Last updated: {time_str}*',
        ]
        + rendered_info_list
    )
    File(readme_file).write(content)


def run_single(d):
    try:
        time_sleep = 60 * (1 + random.random())
        log.info(f'Sleeping for {time_sleep}s')
        time.sleep(time_sleep)
        owid_scraper.scrape(d)
        tweeter.tweet(d)
        return dict(name=d['name'])

    except Exception as e:
        log.error(str(e))
        return None


def run():
    init()
    info_list = []
    for d in CONFIG:
        info = run_single(d)
        info_list.append(info)
    write_readme(info_list)


if __name__ == '__main__':
    run()
