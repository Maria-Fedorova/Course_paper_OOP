class Vacancies:
    """
    Класс для работы с вакансиями
    """
    def __init__(self, vacancy):
        """
        Конструктор
        """
        self.id = vacancy.get('id')
        self.name = vacancy.get('name')
        self.area_url = vacancy['area'].get('url')
        self.salary = {'from': vacancy['salary'].get('from'), 'to': vacancy['salary'].get('to'),
                       'currency': vacancy['salary'].get('currency')}
        self.validation()

    @classmethod
    def prepare_data(cls, data, user_input_keyword):
        """
        Получаем данные списком (как параметр функции), проверяем отсутствующие поля
        """
        prepared_data = []
        for vacancy in data:  # vacancy - словарь
            if user_input_keyword.lower() not in vacancy.get('name').lower():
                continue

            if vacancy.get('area') is None:
                vacancy['area'] = {'url': None}

            if vacancy.get('salary') is None:
                vacancy['salary'] = {'from': 0, 'to': 0, 'currency': 'RUR'}

            if vacancy['salary'].get('currency') != 'RUR':
                continue

            prepared_data.append(vacancy)
        return prepared_data

    def __lt__(self, other):
        """
        Сравнение зарплат по признаку <
        """
        if self.salary['from'] < other.salary['from']:
            return True
        else:
            return False

    def __le__(self, other):
        """
        Сравнение зарплат по признаку <=
        """
        if self.salary['from'] <= other.salary['from']:
            return True
        else:
            return False

    def __gt__(self, other):
        """
        Сравнение зарплат по признаку >
        """
        if self.salary['from'] > other.salary['from']:
            return True
        else:
            return False

    def __ge__(self, other):
        """
        Сравнение зарплат по признаку >=
        """
        if self.salary['from'] >= other.salary['from']:
            return True
        else:
            return False

    def __eq__(self, other):
        """
        Сравнение всех полей экземпляра класса
        """
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
        """
        Метод валидации данных по зарплате для экземпляра класса
        """
        if self.salary['from'] is None:
            self.salary['from'] = 0
        if self.salary['from'] <= 0:
            self.salary['from'] = 0
        if self.salary['to'] is None:
            self.salary['to'] = 0
        if self.salary['to'] <= 0:
            self.salary['to'] = 0

    def convert_to_dict(self):
        """
        Превращает экземпляры класса в словарь
        """
        return {"id": self.id, "name": self.name, "area": {"url": self.area_url}, "salary": self.salary}

    @classmethod
    def convert_list_to_list_of_dicts(cls, vacancy_list_1):
        """
        Преобразует список экземпляров класса Vacancies в список словарей
        """
        list_of_vacancies = []
        for x in vacancy_list_1:
            list_of_vacancies.append(x.convert_to_dict())
        return list_of_vacancies

    @classmethod
    def get_vacancy_list(cls, vacancies, keyword):
        """
        Создает список вакансий в удобном для работы формате,
        при этом входной параметр vacancies - список словарей, полученный из json
        """
        user_input_keyword = keyword
        vacancy_list_local = []
        vacancies = cls.prepare_data(vacancies, user_input_keyword)
        for vac in vacancies:
            vacancy_list_local.append(cls(vac))
        return vacancy_list_local

    def __repr__(self):
        """
        Магический метод представления класса в читаемом формате
        """
        return f'ID: {self.id}, NAME: {self.name}, URL: {self.area_url}, SALARY: {self.salary} \n'
