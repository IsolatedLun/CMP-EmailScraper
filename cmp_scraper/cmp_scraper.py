from time import sleep
from requests import get as req_get

from consts import CMP_COOLDOWN, CMP_NEW_URL, CMP_URL
from cmp_scraper.scraper_funcs import (
    get_project_website_url, 
    get_recent_project_urls,
    get_visited_json,
    update_visited_json
)

def cmp_scraper_run(limit: int= 30):
    """
        Wrapper for getting the urls from CMP.
    """
    
    visited = get_visited_json()
    root = req_get(CMP_NEW_URL)
    project_urls = get_recent_project_urls(root.text)

    website_urls = []
    i = 0
    for x in project_urls:
        if i == limit:
            break

        try:
            print(f'[INFO]: Retrieving {x}. ({i + 1}/{limit})')
            sleep(CMP_COOLDOWN)

            root_currency = req_get(CMP_URL + x)
            url = get_project_website_url(root_currency.text)

            if url is None:
                print('[ERR]: No url.')
                continue

            alread_visited = visited.get(url, False)
            visited.setdefault(url, False)

            if not visited[url]:
                website_urls.append(url)
                visited[url] = True
            elif visited[url]:
                print(f'[INFO]: Already have visited.')
            else:
                print(f'[ERR]: Failed.')

            if not alread_visited: # If url has not been visited previusly, enumerate {i}
                i += 1
        except:
            print('[FATAL]: Something went terribly wrong.')

    update_visited_json(visited)
    return website_urls