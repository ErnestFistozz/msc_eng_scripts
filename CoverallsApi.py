from  CoverageApi import CoverageApi
import requests

class CoverallsApi(CoverageApi):
    def __init__(self, repo: str, page = 1, org = 'coverallsapp', branch = 'master') -> None:
        super(CoverallsApi, self).__init__(repo, org, page, branch)
        self.url = f"https://coveralls.io/github/{self._org}/{self._repo}.json?page={self._page}&branch={self._branch}"

    def total_number_of_pages(self) -> int:
        return self.get_api_response()['pages']

    def coverage_date_pair(self) -> list[tuple]:
        response = self.get_api_response()
        coverage_date_results = []
        builds = response['builds']
        if not builds or builds == None: return []
        for build in builds:
            coverage, commit_hash, commit_date = build['covered_percent'], build['commit_sha'], build['created_at']
            if float(coverage) > 0:
                cov_date_pair = tuple()
                cov_date_pair = (commit_date, commit_hash ,coverage)
                coverage_date_results.append(cov_date_pair)
        return coverage_date_results

    def get_api_response(self):
        response = requests.get(self.url)
        return response.json()
    