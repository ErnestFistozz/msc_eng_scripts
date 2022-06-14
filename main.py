import csv
from CoverallsApi import CoverallsApi
from CodeCovApi import CodeCovApi
from scrapper import *


def save_into_file(repo,  coverage_date_date_pair :list[tuple]) -> None:
    csv_file_name = repo + ".csv"
    with open(csv_file_name, "w") as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(["timestamp", "Commit Hash", "Code Coverage"])
        for row in coverage_date_date_pair:
                csv_writer.writerow(row)

if __name__ == '__main__':

    with open('coveralls_repos.txt', 'r') as coveralls_file:
        coveralls_repos = coveralls_file.read().splitlines()
    with open('codecov_repositories.txt','r') as codecov_file:
        codecov_repos = codecov_file.read().splitlines()
    
    intersecting_repos = list(set(coveralls_repos).intersection(codecov_repos))
    print(intersecting_repos)
'''
    for repo in coveralls_repos:
        print(f'current-repo: {repo}')
        cov_instance = CoverallsApi(repo)
        page_counter = 1
        number_of_pages = cov_instance.total_number_of_pages()
        overall_results = []
        while page_counter <= number_of_pages:
            cov_instance = CoverallsApi(repo, page_counter)
            overall_results += cov_instance.coverage_date_pair()
            page_counter += 1
        save_into_file(repo, overall_results)
# compare similar projects in code cove and coveralls
# list(set(coveralls_repos).intersection(apache_repos)) --> will return a list of common projects only

    with open('codecov_repositories.txt','r') as file:
       apache_repos = file.read().splitlines()
    for repo in apache_repos:
        empty_response = False
        response_counter = 1
        total_cov_date = []
        while not empty_response:
            project = CodeCovApi(repo,response_counter)
            current_response = project.get_api_response()['commits']
            if len(current_response) == 0:
                empty_response = True
            else:
                total_cov_date += project.coverage_date_pair()
            response_counter += 1
        print(f"repo-name: {repo}")
        save_into_file(repo, total_cov_date)
'''