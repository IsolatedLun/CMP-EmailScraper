from bs4 import BeautifulSoup
import json

from consts import CURRENCY_WEBSITE_SELECTOR, TABLE_SELECTOR, VISITED_DIR


def get_recent_project_urls(html: str):
    """
        Gets the recent project urls from CoinMarketCap.
    """

    bs4 = BeautifulSoup(html, 'lxml')

    link_tags = bs4.select(TABLE_SELECTOR)
    
    links = [x.get('href', None) for x in link_tags]

    # Filters None values
    return list(filter(lambda x: x is not None, links))


def get_project_website_url(html: str):
    """
        Gets a project's website url from CoinMarketCap/currency.
    """
    
    bs4 = BeautifulSoup(html, 'lxml')
    link_tag = bs4.select(CURRENCY_WEBSITE_SELECTOR)

    # Returns None if the supposed <a> tag doesn't have a link
    # In that case it's actually a dropdown menu
    return link_tag[0].get('href', None) if len(link_tag) else None

def get_visited_json():
    """
        Gets already visited links from pre-defined json file
    """

    with open(VISITED_DIR, 'r+', encoding='utf-8') as json_file: 
        return json.loads(json_file.read())

def update_visited_json(data):
    """
        Updates the visited json file.
    """
    
    with open(VISITED_DIR, 'r+', encoding='utf-8') as json_file: 
        json.dump(data, json_file)