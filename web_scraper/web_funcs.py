from bs4 import BeautifulSoup
import json
import re
from requests import get as req_get

from consts import EMAILS_DIR

def get_email_addreses(html: str):
    """
        Gets the email addresses from a website.

        Uses regex and selectors.
    """

    def clean_email(x: str):
        if x.startswith('mailto'):
            return x[7::]
        return x
    
    bs4 = BeautifulSoup(html, 'lxml')
    emails = []

    def get_by_regex():
        try: return re.findall(r'[a-z0-9]+@\S+.com', html)
        except: return []

    def get_by_selectors():
        return [clean_email(x['href']) for x in bs4.select('a[href*="mailto"]')]

    emails.extend(get_by_regex())
    emails.extend(get_by_selectors())

    return list(set(emails)) # Remove duplicates
    
def update_emails(emails: list[str]):
        _emails = []; _emails.extend(emails)

        with open(EMAILS_DIR, 'r', encoding='utf-8') as json_file: 
            _emails.extend(json.load(json_file))

        with open(EMAILS_DIR, 'w+', encoding='utf-8') as json_file: 
            json.dump(_emails, json_file, indent=2)

def req_safe_get(url: str):
    res = None

    if not url.startswith('http') or not url.startswith('https'):
        try:
            res = req_get('https://' + url)
        except:
            res = req_get('http://' + url)

    return res