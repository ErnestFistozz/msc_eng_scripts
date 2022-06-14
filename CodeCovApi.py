
from CoverageApi import CoverageApi
import requests

class CodeCovApi(CoverageApi):
    def __init__(self, repo : str, page : int, org='apache', branch='master', limit = 20) -> None:
        super(CodeCovApi, self).__init__(repo, org, page, branch)
        self._limit = limit
        self.url = f"https://codecov.io/api/gh/{self._org}/{self._repo}/branch/{self._branch}/commits?page={self._page}&limit={self._limit}"

    def get_api_response(self) :
        response = requests.get(self.url)
        return response.json()

    def coverage_date_pair(self) -> list[tuple]:
        coverage_date_pair = []
        commits = self.get_api_response()['commits']
        if len(commits) == 0 or commits == None: return []
        for commit in commits:
            if not isinstance(commit['totals'], type(None)):
                    coverage, commit_hash, commit_date = commit['totals']['c'], commit['commitid'], commit['timestamp']
                    if not isinstance(coverage, type(None)):
                        if float(coverage) > 0:
                            cov_time_pair = tuple()
                            cov_time_pair  = (commit_date, commit_hash, coverage)
                            coverage_date_pair.append(cov_time_pair)
        return coverage_date_pair

        