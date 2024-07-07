import os
import requests
import json
from abc import ABC, abstractmethod


class Parser(ABC):


    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class AbstractJsonSaver(ABC):

    @abstractmethod
    def save_file(self, data: list):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def add_vacancy_to_file(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
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
        return vacancies


class Vacancies:
    """
    Класс для работы с вакансиями
    """

    vacancy_list = [] #список экземпляров класса в нужном формате моего класса

    def __repr__(self):
        return f'ID: {self.id}, NAME: {self.name}, URL: {self.area_url}, SALARY: {self.salary} \n'

    def __init__(self, vacancy):
        self.id = vacancy.get('id')
        self.name = vacancy.get('name')
        self.area_url = vacancy['area'].get('url')
        self.salary = {'from': vacancy['salary'].get('from'), 'to': vacancy['salary'].get('to'),
                                         'currency': vacancy['salary'].get('currency')}
        self.validation()
        self.vacancy_list.append(self)

    @classmethod
    def prepare_data(cls, data):
        """Получаем данные списком (как параметр функции), проверяем отсутствующие поля"""
        prepared_data = []
        for vacancy in data: #vacancy - словарь
            if vacancy.get('area') is None:
                vacancy['area'] = {'url': None}

            if vacancy.get('salary') is None:
                vacancy['salary'] = {'from': 0, 'to': 0, 'currency': ''}

            prepared_data.append(vacancy)
        return prepared_data

    def __lt__(self, other):
        if self.salary['from'] < other.salary['from']:
            return True
        else:
            return False

    def __le__(self, other):
        if self.salary['from'] <= other.salary['from']:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.salary['from'] > other.salary['from']:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.salary['from'] >= other.salary['from']:
            return True
        else:
            return False

    def validation(self):
        if self.salary['from'] is None:
            self.salary['from'] = 0
        if self.salary['from'] <= 0:
            self.salary['from'] = 0
        if self.salary['to'] is None:
            self.salary['to'] = 0
        if self.salary['to'] <= 0:
            self.salary['to'] = 0

    def convert_to_dict(self):
        "Превращает экземпляры класса в словарь"
        return {'ID': self.id, "NAME": self.name, "URL": self.area_url, 'SALARY': self.salary}

    def convert_to_list_of_dicts(self):
        list_of_vacancies = []
        for x in self.vacancy_list:
            list_of_vacancies.append(x.convert_to_dict())
        return list_of_vacancies


    @classmethod
    def get_vacancy_list(cls, vacancies):

        """
        Создает список вакансий
        vacancies - список словарей, полученный из json
        """

        vacancies = cls.prepare_data(vacancies)
        for vac in vacancies:
            cls(vac)
        return cls.vacancy_list


class JsonSaver(AbstractJsonSaver):

    def save_file(self, data: list):
        """Save file"""
        print(type(data))
        list_to_file1 = [d.convert_to_dict() for d in data]
        if os.path.exists('vacancies.json'):
            os.remove('vacancies.json')
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(list_to_file1, file, indent=2, ensure_ascii=False)


    def read_file(self):
        """Read file"""
        with open('vacancies.json', encoding='utf-8') as file:
            return json.load(file)

    def add_vacancy_to_file(self, data):
        list_to_file2 = [d.convert_to_dict() for d in data]
        list2 = self.read_file()
        list2.extend(list_to_file2)
        os.remove('vacancies.json')
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(list2, file, indent=2, ensure_ascii=False)

    def delete_vacancy(self, vacancy: str):
        new_list = []

        old_list = self.read_file()

        for params in old_list:
            if params['NAME'] != vacancy:
                new_list.append(params)

        os.remove('vacancies.json')
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(new_list, file, indent=2, ensure_ascii=False)
