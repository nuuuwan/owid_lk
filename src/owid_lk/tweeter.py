from utils import tsv, twitter

from owid_lk._utils import get_data_dir, get_data_file, get_image_file, get_url

DELIMITER = ','


def tweet(d):
    get_data_dir()
    png_file = get_image_file(d)

    func_get_tweet_text = d.get('func_get_tweet_text', None)
    inner_tweet_text = ''
    if func_get_tweet_text:
        data_file = get_data_file(d)
        data_list = tsv.read(data_file, delimiter=DELIMITER)
        inner_tweet_text = func_get_tweet_text(data_list)

    name_str = d['name'].replace('-', ' ').title()
    name_str = name_str.replace('Covid ', '#COVID19 ')
    name_str = name_str.replace('Covid19 ', '#COVID19 ')
    url = get_url(d)
    tweet_text = f'''{name_str}
via @OurWorldInData

{inner_tweet_text}

#COVID19SL #SriLanka #lka
Source: {url}
    '''
    status_image_files = [png_file]

    tweet_text = tweet_text.replace("\n" * 4, "\n" * 2)

    twtr = twitter.Twitter.from_args()
    twtr.tweet(
        tweet_text=tweet_text,
        status_image_files=status_image_files,
        update_user_profile=True,
    )
