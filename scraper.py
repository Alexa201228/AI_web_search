import requests
from bs4 import BeautifulSoup
import csv


class Scraper:

    def __init__(self, query: str, num_of_pages: int) -> None:
        self._query = query
        self._num_of_pages = num_of_pages

    def get_source(self, url):
        try:
            usr_agent = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
            response = requests.get(url, headers=usr_agent)
            return response

        except requests.exceptions.RequestException as e:
            print(e)

    def get_results(self):
        term = self._query.lower().replace(' ', '+')
        response = self.get_source(f"https://www.google.com/search?q={term}&num={self._num_of_pages}")

        return response

    def parse_results(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        result_block = soup.find_all('div', attrs={'class': 'g'})
        output = dict()
        for result in result_block:
            # Find link, title, description
            link = result.find('a', href=True)
            title = result.find('h3')
            description_box = result.find('div', {'style': '-webkit-line-clamp:2'})
            if description_box:
                description = description_box.find('span')
                if link and title and description and not link['href'] in output:
                    output[link['href']] = [link['href'], title.text, description.text]
        self.create_data_set(output.values())

    def create_data_set(self, arr_data):
        with open('fetched_data.csv', 'w', encoding='cp1251', errors='replace') as file:
            writer = csv.writer(file)
            writer.writerows(arr_data)



