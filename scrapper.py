from requests_html import HTMLSession

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
req_headers = {"User-Agent": user_agent,
           'Accept': 'text/html',
           'Accept-Language': 'en-US,en;q=0.5',
           'DNT': '1',
           'Connection': 'keep-alive',
           'Upgrade-Insecure-Requests': '1'
           }
'''
url = f'https://coveralls.io/github/apache?page=1'
res = session.get(url, headers = req_headers)

page_repos_elements = res.html.find('div.repoChartInfo')
chained_arr = page_repos_elements[0].find('a')
actual_data = chained_arr[1].find('a').text
#print(actual_data[0].text)

'''
def coveralls_projects(total_pages: int, org: str ) -> list[str]:
    current_page = 1
    repo_names = []
    while current_page <= total_pages:
        session  = HTMLSession()
        url  = f'https://coveralls.io/github/{org}?page={current_page}'
        res = session.get(url, headers = req_headers)
        page_repos_elements = res.html.find('div.repoChartInfo')
        for repo in page_repos_elements:
            data = repo.find('a')
            if not data:
                continue
            else:
                org_project_name = data[1].find('a')
                repo_names.append(org_project_name[0].text)
        current_page += 1
    return repo_names

if __name__ == '__main__':
    org = 'apache'
    total_no_of_pages = 4
    projects = coveralls_projects(total_no_of_pages, org)
