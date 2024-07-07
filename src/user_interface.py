from src.classes_API import HH
from src.classes_Vacancies import Vacancies


def interaction():
    user_input = input("Введите название профессии для запроса вакансий из hh.ru. Например, programmer \n")
    hh = HH()
    x = hh.load_vacancies(user_input)
    vacan = Vacancies.get_vacancy_list(x)
    if user_input.isalpha():  # and user_input in vacan['name']
        vacan.sort(reverse=True)
    else:
        return "Вы ввели некорректный запрос"

    user_input = int(input("Введите количество вакансий (Х) для списка ТОП-Х \n"))
    top_x = vacan[0:user_input]
    print (top_x)
