from src.classes_API import HH

def test_load_vacancies():
    y = HH()
    x = y.load_vacancies('go')
    assert type(x) == list
    assert type(x[0]) == dict
    assert y.get_params().get('page') <= 3

    