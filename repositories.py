
import requests, csv
from scrapper import *

def apache_repos(org = 'apache') -> list[str]:
    empty = False
    page = 1
    names_of_repos = []
    while not empty:
        url = f"https://codecov.io/api/gh/{org}?page={page}&limit=20"
        res = requests.get(url)
        repos = res.json()['repos']
        if not repos:
            empty = True
            continue
        for repo in repos:
            if repo['language'] == 'java' or isinstance(repo['language'], type(None)):
                if not isinstance(repo['name'], type(None)):
                    names_of_repos.append(repo['name'])
        page +=1
    return names_of_repos
'''
    Code Cov:  https://codecov.io/api/gh/apache?page=1
    Coveralls: https://coveralls.io/github/apache?page=2
'''

def text_file(cov_tool: str, repositories : list[str]) -> None:
    with open(f'{cov_tool}.txt', 'w') as file:
        for repo in repositories:
            file.write(repo + "\n")

def main():
    code_cov = 'code_cov_repos'
    coveralls_cov = 'coveralls_repos'
    coveralls_org = 'apache'
    total_number_of_pages = 4
    #text_file(code_cov, apache_repos())
    text_file(coveralls_cov, coveralls_projects(total_number_of_pages, coveralls_org))


if __name__ == '__main__':
    main()
