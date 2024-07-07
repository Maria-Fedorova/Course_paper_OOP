import requests
from abc import ABC, abstractmethod


class Parser(ABC):


    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    def load_vacancies(self, keyword):
        self.__params['text'] = keyword
        while self.__params.get('page') != 3:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1
        return vacancies #список словарей


    def get_params(self):
        return self.__params