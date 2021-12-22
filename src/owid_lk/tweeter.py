import os
from utils import timex, twitter
from owid_lk._utils import get_data_dir, get_url


def tweet(d):
    data_dir = get_data_dir()
    png_file = os.path.join(data_dir, d['name'] + '.png')

    name_str = d['name'].replace('-', ' ').title()
    url = get_url(d)
    tweet_text = f'''{name_str} via @OurWorldInData

Source: {url}
    '''
    status_image_files = [png_file]

    twtr = twitter.Twitter.from_args()
    twtr.tweet(
        tweet_text=tweet_text,
        status_image_files=status_image_files,
        update_user_profile=True,
    )
