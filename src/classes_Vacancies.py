class Vacancies:
    """
    Класс для работы с вакансиями
    """

    #vacancy_list = [] #список экземпляров класса в нужном формате моего класса

    def __repr__(self):
        return f'ID: {self.id}, NAME: {self.name}, URL: {self.area_url}, SALARY: {self.salary} \n'

    def __init__(self, vacancy):
        self.id = vacancy.get('id')
        self.name = vacancy.get('name')
        self.area_url = vacancy['area'].get('url')
        self.salary = {'from': vacancy['salary'].get('from'), 'to': vacancy['salary'].get('to'),
                                         'currency': vacancy['salary'].get('currency')}
        self.validation()
        #self.vacancy_list.append(self)

    @classmethod
    def prepare_data(cls, data):
        """Получаем данные списком (как параметр функции), проверяем отсутствующие поля"""
        prepared_data = []
        for vacancy in data: #vacancy - словарь
            if vacancy.get('area') is None:
                vacancy['area'] = {'url': None}

            if vacancy.get('salary') is None:
                vacancy['salary'] = {'from': 0, 'to': 0, 'currency': ''}

            if vacancy['salary'].get('currency') != 'RUR':
                continue

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

    def __eq__(self, other):
        """Сравниваем все поля"""
        result = True

        if self.id != other.id:
            result = False
        if self.name != other.name:
            result = False
        if self.area_url != other.area_url:
            result = False
        if self.salary['from'] != other.salary['from']:
            result = False
        if self.salary['to'] != other.salary['to']:
            result = False
        if self.salary['currency'] != other.salary['currency']:
            result = False
        return result

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
        return {"id": self.id, "name": self.name, "area":{"url": self.area_url}, "salary": self.salary}

    # def convert_to_list_of_dicts(self):
    #     """Преобразует список экземпляров класса Vacancies в список словарей"""
    #     list_of_vacancies = []
    #     for x in self.vacancy_list:
    #         list_of_vacancies.append(x.convert_to_dict())
    #     return list_of_vacancies

    @classmethod
    def convert_list_to_list_of_dicts(cls, vacancy_list_1):
        """Преобразует список экземпляров класса Vacancies в список словарей"""
        list_of_vacancies = []
        for x in vacancy_list_1:
            list_of_vacancies.append(x.convert_to_dict())
        return list_of_vacancies


    @classmethod
    def get_vacancy_list(cls, vacancies):

        """
        Создает список вакансий
        vacancies - список словарей, полученный из json
        """
        vacancy_list_local = []
        vacancies = cls.prepare_data(vacancies)
        for vac in vacancies:
            vacancy_list_local.append(cls(vac))
        return vacancy_list_local
