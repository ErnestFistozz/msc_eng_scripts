import requests
import json
import csv

# due to multiple versions of python : execute this with
# /usr/local/opt/python@3.9/bin/python3.9 <script-name>
# e.g /usr/local/opt/python@3.9/bin/python3.9 codecov.py

def codecov(repo, page, org="apache", branch="master", limit=20):
    url = f"https://codecov.io/api/gh/{org}/{repo}/branch/{branch}/commits?page={page}&limit={limit}"
    response = requests.get(url)
    return response.json()

def coverage_date_metrics(res) -> list:
    coverage_date_pair = []
    commits = res['commits']
    if len(res) != 0:
        for commit in commits:
            coverage, commit_date = commit['totals']['c'], commit['timestamp']
            cov_time_pair = tuple()
            cov_time_pair = (commit_date,coverage)
            coverage_date_pair.append(cov_time_pair)
    return coverage_date_pair


def save_into_file(repo : str, coverage_timestamp : list):
    csv_file_name = repo + ".csv"
    with open(csv_file_name, "w") as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(["timestamp", "Code Coverage"])
        for row in coverage_timestamp:
            csv_writer.writerow(row)

if __name__ == "__main__":
    repo_name = "dubbo"
    #repositories = []
    #for repo in repositories:
    is_empty_response = False
    response_counter = 1
    total_coverage_time_pair = []
    while is_empty_response == False:
        res = codecov(repo_name, response_counter)
        if len(res) == 0:
            is_empty_response = True
            break
        else:
            result = coverage_date_metrics(res)
            total_coverage_time_pair += result
            response_counter += 1
    
    save_into_file(repo_name, total_coverage_time_pair)
