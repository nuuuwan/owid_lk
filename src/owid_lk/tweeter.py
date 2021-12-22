import os

from owid_lk._utils import get_data_dir


def tweet(d):
    data_dir = get_data_dir()
    png_file = os.path.join(data_dir, d['name'] + '.png')
    print(png_file)
