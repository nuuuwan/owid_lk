import os

from utils import tsv, twitter

from owid_lk._utils import get_data_dir, get_url

DELIMITER = ','


def tweet(d):
    data_dir = get_data_dir()
    png_file = os.path.join(data_dir, d['name'] + '.png')
    csv_file = os.path.join(data_dir, d['name'] + '.csv')
    data_list = tsv.read(csv_file, delimiter=DELIMITER)
    inner_tweet_text = d['func_get_tweet_text'](data_list)

    name_str = d['name'].replace('-', ' ').title()
    url = get_url(d)
    tweet_text = f'''{name_str}
via @OurWorldInData

{inner_tweet_text}

Source: {url}
    '''
    status_image_files = [png_file]

    twtr = twitter.Twitter.from_args()
    twtr.tweet(
        tweet_text=tweet_text,
        status_image_files=status_image_files,
        update_user_profile=True,
    )
