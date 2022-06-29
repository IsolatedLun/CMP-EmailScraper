from requests import get as req_get
from web_scraper.web_funcs import get_email_addreses, update_emails

def web_scraper_run(url: str):
    """
        Wrapper for getting emails from websites.
    """

    print(f'[INFO]: Scraping from {url}.')
    req = req_get(url)

    if req.status_code < 400:
        addresses = get_email_addreses(req.text)
        
        update_emails(addresses)
    else:
        print(f'[ERR]: Failed accessing {url}.\n')