from src.classes_API import HH


def test_load_vacancies():
    """
    Тест метода, который возвращает список словарей, состоящих из вакансий, полученных с сайта HH
    """
    y = HH()
    x = y.load_vacancies('go')
    assert type(x) is list
    assert type(x[0]) is dict
    assert y.get_params().get('page') <= 3
