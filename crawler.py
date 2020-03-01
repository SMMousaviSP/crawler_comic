import os
import requests
from bs4 import BeautifulSoup


# Enter the path you want to save your comics
PATH_TO_COMIC = '/tmp/'


def normalize_string(raw_string):
    """ Normalize string by replacing all spaces with '_' and change all
    characters to lower case.

    :param raw_string: Input string to be normalized.
    :returns: Normalized string without uppercase or space.

    """
    return raw_string.strip().lower().replace(' ', '_').replace('/', '_').replace('\\', '_')


def mkdir(dir_name):
    """ Create directory in PATH_TO_COMIC location if it's not already exists.

    :param dir_name: Directory name.
    :returns: Void.

    """
    dir_name = PATH_TO_COMIC + dir_name
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def get_soup(url):
    """ Create a soup object for crawling.
    :param url: Url of page for crawling.
    :returns: Soup object for crawling.

    """
    return BeautifulSoup(requests.get(url).text, 'html.parser')
