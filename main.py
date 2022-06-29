from cmp_scraper.cmp_scraper import cmp_scraper_run
from web_scraper.web_scraper import web_scraper_run

from consts import LIMIT

if __name__ == '__main__':
    urls = cmp_scraper_run(LIMIT)
    
    for x in urls:
        web_scraper_run(x)
    print('[INFO]: DONE')