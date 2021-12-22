from utils import filex, timex

from owid_lk import owid_scraper, tweeter
from owid_lk._utils import get_url, init
from owid_lk.CONFIG import CONFIG


def write_readme():
    readme_file = '/tmp/README.md'
    time_str = timex.format_current_date_with_timezone()
    content = '\n\n'.join(
        [
            '# Our World in Data (Sri Lanka)',
            f'*Last updated: {time_str}*',
        ]
    )
    filex.write(readme_file, content)


if __name__ == '__main__':
    init()

    for d in CONFIG:
        url = get_url(d)
        owid_scraper.scrape(url)
        tweeter.tweet(d)
        write_readme()
