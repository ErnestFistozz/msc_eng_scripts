
import requests, csv

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
            if repo['language'] == 'java':
                if not isinstance(repo['name'], type(None)):
                    names_of_repos.append(repo['name'])
        page +=1
    return names_of_repos
'''
    Code Cov: https://codecov.io/api/gh/apache?page=1
    Coveralls: https://coveralls.io/github/apache?page=2
'''

def coveralls_repos(org ='apache') -> list[str]:
    return


def text_file(repositories : list[str]) -> None:
    with open('codecov_repositories.txt', 'w') as file:
        for repo in repositories:
            file.write(repo + "\n")

def main():
    text_file(apache_repos())


if __name__ == '__main__':
    main()