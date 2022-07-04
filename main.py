from cmp_scraper.cmp_scraper import cmp_scraper_run
from web_scraper.web_funcs import update_emails
from web_scraper.web_scraper import web_scraper_run

from consts import LIMIT

if __name__ == '__main__':
    urls = cmp_scraper_run(LIMIT)
    emails = []
    
    for x in urls:
        emails.extend(web_scraper_run(x))

    update_emails(emails)
    print('[INFO]: DONE')