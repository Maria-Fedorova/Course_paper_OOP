import pytest
from src.classes_Vacancies import Vacancies


@pytest.fixture
def corrupted_data():
    x = [
        {
            "id": "102647120_Тест",
            "name": "Бухгалтер_Тест",
            "salary": {
                "from": 400000,
                "to": 0,
                "currency": "KZT"
            }
        },
        {
            "id": "100711654_Тест",
            "name": "Архитектор_Тест",
            "area": {"url": "https://api.hh.ru/areas/1"},
        },
        {
            "id": "100711654_Тест",
            "name": "Архитектор_Тест",
            "area": {"url": "https://api.hh.ru/areas/1"},
            "salary": {
                "from": 200000,
                "to": 400000,
                "currency": "RUR"
            }
        }
    ]
    return x


@pytest.fixture
def correct_data():
    x = [
        {
            "id": "100711654_Тест",
            "name": "Архитектор_Тест",
            "area": {"url": "https://api.hh.ru/areas/1"},
            "salary": {
                "from": 0,
                "to": 0,
                "currency": "RUR"
            }
        },
        {
            "id": "100711654_Тест",
            "name": "Архитектор_Тест",
            "area": {"url": "https://api.hh.ru/areas/1"},
            "salary": {
                "from": 200000,
                "to": 400000,
                "currency": "RUR"
            }
        }
    ]
    return x


@pytest.fixture
def invalid_data():
    x = [
        {
            "id": "102647120_Тест",
            "name": "Бухгалтер_Тест",
            "area": {"url": "https://api.hh.ru/areas/1"},
            "salary": {
                "from": 0,
                "to": 0,
                "currency": "KZT"
            }
        },
        {
            "id": "100711654_Тест",
            "name": "Менеджер по развитию бизнеса (BDM)_Тест",
            "area": {"url": "https://api.hh.ru/areas/1"},
            "salary": {
                "from": 0,
                "to": 0,
                "currency": ""
            }
        }
    ]
    list_of_invalid_data = [Vacancies(y) for y in x]
    list_of_invalid_data[0].salary["from"] = None
    list_of_invalid_data[0].salary["to"] = None
    list_of_invalid_data[1].salary["from"] = -100
    list_of_invalid_data[1].salary["to"] = -100
    return list_of_invalid_data


@pytest.fixture
def valid_data():
    x = [
        {
            "id": "102647120_Тест",
            "name": "Бухгалтер_Тест",
            "area": {"url": "https://api.hh.ru/areas/1"},
            "salary": {
                "from": 0,
                "to": 0,
                "currency": "KZT"
            }
        },
        {
            "id": "100711654_Тест",
            "name": "Менеджер по развитию бизнеса (BDM)_Тест",
            "area": {"url": "https://api.hh.ru/areas/1"},
            "salary": {
                "from": 0,
                "to": 0,
                "currency": ""
            }
        }
    ]
    list_of_valid_data = [Vacancies(y) for y in x]
    return list_of_valid_data


@pytest.fixture
def vacancies():
    x = [
            {
              "id": "102647120_Тест",
              "name": "Бухгалтер_Тест",
              "area": {"url": "https://api.hh.ru/areas/159"},
              "salary": {
                "from": 50000,
                "to": 0,
                "currency": "RUR"
              }
            },
            {
              "id": "100711654_Тест",
              "name": "Менеджер по развитию бизнеса (BDM)_Тест",
              "area": {"url": "https://api.hh.ru/areas/1"},
              "salary": {
                "from": 400000,
                "to": 0,
                "currency": "RUR"
              }
            },
            {
              "id": "102647120_Тест",
              "name": "Архитектор_Тест",
              "area": {"url": "https://api.hh.ru/areas/159"},
              "salary": {
                "from": 200000,
                "to": 0,
                "currency": "RUR"
              }
            },
            {
              "id": "100711654_Тест",
              "name": "Водитель_Тест",
              "area": {"url": "https://api.hh.ru/areas/1"},
              "salary": {
                "from": 50000,
                "to": 0,
                "currency": "RUR"
              }
            }
          ]
    return Vacancies.get_vacancy_list(x, '')


@pytest.fixture
def vacancies_dict():
    x = [
            {
              "id": "102647120_Тест",
              "name": "Бухгалтер_Тест",
              "area": {"url": "https://api.hh.ru/areas/159"},
              "salary": {
                "from": 50000,
                "to": 0,
                "currency": "RUR"
              }
            },
            {
              "id": "100711654_Тест",
              "name": "Менеджер по развитию бизнеса (BDM)_Тест",
              "area": {"url": "https://api.hh.ru/areas/1"},
              "salary": {
                "from": 400000,
                "to": 0,
                "currency": "RUR"
              }
            },
            {
              "id": "102647120_Тест",
              "name": "Архитектор_Тест",
              "area": {"url": "https://api.hh.ru/areas/159"},
              "salary": {
                "from": 200000,
                "to": 0,
                "currency": "RUR"
              }
            },
            {
              "id": "100711654_Тест",
              "name": "Водитель_Тест",
              "area": {"url": "https://api.hh.ru/areas/1"},
              "salary": {
                "from": 50000,
                "to": 0,
                "currency": "RUR"
              }
            }
          ]
    return x


def test_prepare_data(corrupted_data, correct_data):
    """
    Тест метода, который получает данные списком (как параметр функции) и проверяет отсутствующие поля
    """
    keyword = 'архитектор'
    assert Vacancies.prepare_data(corrupted_data, keyword) == correct_data


def test__lt__(vacancies):
    """
    Тест сравнения зарплат по признаку <
    """
    list_of_vacancies = vacancies
    assert (list_of_vacancies[0] < list_of_vacancies[1]) is True
    assert (list_of_vacancies[1] < list_of_vacancies[0]) is False


def test__le__(vacancies):
    """
    Тест сравнения зарплат по признаку <=
    """
    list_of_vacancies = vacancies
    assert (list_of_vacancies[0] <= list_of_vacancies[1]) is True
    assert (list_of_vacancies[1] <= list_of_vacancies[0]) is False
    assert (list_of_vacancies[0] <= list_of_vacancies[3]) is True


def test__gt__(vacancies):
    """
    Тест сравнения зарплат по признаку >
    """
    list_of_vacancies = vacancies
    assert (list_of_vacancies[1] > list_of_vacancies[0]) is True
    assert (list_of_vacancies[0] > list_of_vacancies[1]) is False


def test__ge__(vacancies):
    """
    Тест сравнения зарплат по признаку >=
    """
    list_of_vacancies = vacancies
    assert (list_of_vacancies[1] >= list_of_vacancies[0]) is True
    assert (list_of_vacancies[0] >= list_of_vacancies[1]) is False
    assert (list_of_vacancies[0] >= list_of_vacancies[3]) is True


def test_validation(invalid_data, valid_data):
    """
    Тест метода валидации данных по зарплате для экземпляра класса
    """
    list_of_invalid_data = invalid_data
    list_of_valid_data = valid_data
    for x in list_of_invalid_data:
        x.validation()
    assert list_of_valid_data == list_of_invalid_data


def test_convert_to_dict(valid_data):
    """
    Тест метода, который превращает экземпляры класса в словарь
    """
    x = valid_data[0]
    assert x.convert_to_dict() == {"id": x.id, "name": x.name, "area": {"url": x.area_url}, "salary": x.salary}


def test_convert_list_to_list_of_dicts(vacancies_dict):
    """
    Тест метода, который преобразует список экземпляров класса Vacancies в список словарей
    """
    list_of_dicts = vacancies_dict
    list_of_vac = Vacancies.get_vacancy_list(list_of_dicts, '')
    assert Vacancies.convert_list_to_list_of_dicts(list_of_vac) == list_of_dicts


def test_get_vacancy_list(vacancies_dict):
    """
    Тест метода, который создает список вакансий в удобном для работы формате
    """
    vac = Vacancies.get_vacancy_list(vacancies_dict, '')
    test_vac = [Vacancies(x) for x in vacancies_dict]
    assert vac == test_vac
