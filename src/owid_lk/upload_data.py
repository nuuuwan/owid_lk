from utils import filex, timex

from owid_lk import owid_scraper, tweeter
from owid_lk._utils import init
from owid_lk.CONFIG import CONFIG


def write_readme(info_list):
    readme_file = '/tmp/README.md'
    time_str = timex.format_current_date_with_timezone()

    rendered_info_list = list(
        map(
            lambda info: '* %s' % (info['name']),
            info_list,
        )
    )
    content = '\n\n'.join(
        [
            '# Our World in Data (Sri Lanka)',
            f'*Last updated: {time_str}*',
        ]
        + rendered_info_list
    )
    filex.write(readme_file, content)


def run_prod():
    init()

    info_list = []
    for d in CONFIG:
        owid_scraper.scrape(d)
        tweeter.tweet(d)
        info_list.append(dict(name=d['name']))
    write_readme(info_list)


def run_test_tweet():
    init()

    for d in CONFIG:
        tweeter.tweet(d)


if __name__ == '__main__':
    run_prod()
