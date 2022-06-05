class CoverageApi:

    def __init__(self, init_repo : str, init_org: str, init_page : int, init_branch : str) -> None:
        self._repo = init_repo
        self._branch = init_branch
        self._org = init_org
        self._page = init_page

    def coverage_date_pair(self) -> list[tuple]:
        pass
    
    def get_api_response(self):
        pass
