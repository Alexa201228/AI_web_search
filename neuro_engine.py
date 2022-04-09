from __future__ import annotations

import os
import queue
import shutil
import threading

from scraper import Scraper
from tensorflow_search import TensorSemanticSearch


class AgentsSearch:
    _my_queue: queue.Queue = queue.Queue()

    def __init__(self, agents_count: int, user_request: str):
        self._agents_count = agents_count
        self._user_request = user_request.lower()

    def search(self):
        scraper = Scraper(self._user_request, 5000)
        results = scraper.get_results()
        scraper.parse_results(results)
        semantic_search = TensorSemanticSearch()
        agents_dict = {}
        for fname in os.listdir('.'):
            if fname.startswith('temp'):
                shutil.rmtree(fname)
        threads = []
        for i in range(self._agents_count):
            t = threading.Thread(target=semantic_search.find_closest_answers, args=[self._user_request, f'temp{i}', self._my_queue], daemon=True)
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()
        i = 1
        while not self._my_queue.empty():
            result = self._my_queue.get()
            agents_dict[f'Agent {i}'] = result
            i += 1
        for fname in os.listdir('.'):
            if fname.startswith('temp'):
                shutil.rmtree(fname)
        return agents_dict