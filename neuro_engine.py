from __future__ import annotations
from scraper import Scraper
from tensorflow_search import TensorSemanticSearch


class AgentsSearch:

    def __init__(self, agents_count: int, user_request: str):
        self._agents_count = agents_count
        self._user_request = user_request.lower()

    def search(self):
        scraper = Scraper(self._user_request, 1000)
        results = scraper.get_results()
        parsed_data = scraper.parse_results(results)
        semantic_search = TensorSemanticSearch()
