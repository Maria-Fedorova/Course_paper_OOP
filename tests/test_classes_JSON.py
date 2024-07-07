import pytest
from src.classes_Vacancies import Vacancies
from src.classes_JSON import JsonSaver


@pytest.fixture
def vacancies():
    x = [
            {
              "id": "102647120_Тест",
              "name": "Бухгалтер_Тест",
              "area":{"url": "https://api.hh.ru/areas/159"},
              "salary": {
                "from": 400000,
                "to": 0,
                "currency": "KZT"
              }
            },
            {
              "id": "100711654_Тест",
              "name": "Менеджер по развитию бизнеса (BDM)_Тест",
              "area":{"url": "https://api.hh.ru/areas/1"},
              "salary": {
                "from": 400000,
                "to": 0,
                "currency": "RUR"
              }
            }
          ]
    return Vacancies.get_vacancy_list(x)


@pytest.fixture
def vacancies_2():
    x = [
            {
              "id": "102647120_Тест",
              "name": "Архитектор_Тест",
              "area":{"url": "https://api.hh.ru/areas/159"},
              "salary": {
                "from": 400000,
                "to": 0,
                "currency": "KZT"
              }
            },
            {
              "id": "100711654_Тест",
              "name": "Водитель_Тест",
              "area":{"url": "https://api.hh.ru/areas/1"},
              "salary": {
                "from": 400000,
                "to": 0,
                "currency": "RUR"
              }
            }
          ]
    return Vacancies.get_vacancy_list(x)


def test_save_read_file(vacancies):
    test_vacancies = vacancies
    JsonSaver.save_file(test_vacancies)
    list_of_dicts = Vacancies.convert_list_to_list_of_dicts(test_vacancies)
    assert list_of_dicts == JsonSaver.read_file()


def test_add_vacancy_to_file(vacancies, vacancies_2):
    test_vacancies = vacancies
    test_vacancies_2 = vacancies_2
    saver = JsonSaver()
    saver.save_file(test_vacancies)
    saver.add_vacancy_to_file(test_vacancies_2)
    test_vacancies = test_vacancies + test_vacancies_2
    list_of_dicts = Vacancies.convert_list_to_list_of_dicts(test_vacancies)
    assert list_of_dicts == saver.read_file()


def test_delete_vacancy(vacancies):
    test_vacancies = vacancies
    saver = JsonSaver()
    saver.save_file(test_vacancies)
    saver.delete_vacancy(test_vacancies[0].name)
    test_vacancies.pop(0)
    list_of_dicts = Vacancies.convert_list_to_list_of_dicts(test_vacancies)
    assert list_of_dicts == saver.read_file()
