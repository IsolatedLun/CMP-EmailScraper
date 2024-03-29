from requests import get as req_get
from consts import WEB_COOLDOWN
from web_scraper.web_funcs import get_email_addreses, update_emails
from time import sleep

def web_scraper_run(url: str):
    """
        Wrapper for getting emails from websites.
    """

    print(f'[INFO]: Scraping from {url}.')
    try:
        req = req_get(url)

        if req.status_code < 400:
            addresses = get_email_addreses(req.text)
            print(f'[SUCCESS]: { len(addresses) } emails.')
            sleep(WEB_COOLDOWN) # This is redundant because the website will only be visited once.

            return addresses
        else:
            print(f'[ERR]: Failed accessing {url}.\n')
            return []
    except:
        print(f'[FATAL]: Failed accessing {url}.\n')
        return []