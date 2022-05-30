import json
import csv
import requests

class CommitCodeCov:
    def __init__(self, repo: str, page : int, limit  = 20, branch="master", org="apache") -> None:
        self.repo_name = repo
        self.page = page
        self.page_limit = limit
        self.branch = branch
        self.org = org 
        self.url = f"https://https://codecov.io/api/gh/{self.org}/{self.repo_name}/branch/{self.branch}/commits?page={self.page}&limit={self.page_limit}"
    
    def jsonify_response(self) -> tuple:
        response = requests.get(self.url)
        response_data = json.loads(response)
        code_coverage, date = [], []
        commits = response_data['commits']
        for commit in commits:
            coverage, commit_date = commit['totals']['c'], commit['totals']['timestamp']
            code_coverage.append(coverage)
            date.append(commit_date)

        return tuple(zip(date, code_coverage))

    def store_results_file(self):
        data = list(self.jsonify_response())
        with open(f'{self.repo_name}.csv', 'wb') as out_stream:
            output = csv.write(out_stream)
            output.writerow(['Timestap', 'Code Coverage'])
            for row in data:
                output.writerow(row)

        return