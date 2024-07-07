import os
import json
from abc import ABC, abstractmethod


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


class JsonSaver(AbstractJsonSaver):

    @classmethod
    def save_file(cls, data: list):
        """Save file"""
        print(type(data))
        list_to_file1 = [d.convert_to_dict() for d in data]
        if os.path.exists('vacancies.json'):
            os.remove('vacancies.json')
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(list_to_file1, file, indent=2, ensure_ascii=False)

    @classmethod
    def read_file(cls):
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
            if params['name'] != vacancy:
                new_list.append(params)

        os.remove('vacancies.json')
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(new_list, file, indent=2, ensure_ascii=False)
