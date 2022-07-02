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
            
            update_emails(addresses)
            print(f'[SUCCESS]\n')
            sleep(WEB_COOLDOWN) # This is redundant because the website will only be visited once.
        else:
            print(f'[ERR]: Failed accessing {url}.\n')
    except:
        print(f'[FATAL]: Failed accessing {url}.\n')