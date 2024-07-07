from src.classes_API import HH
from src.classes_Vacancies import Vacancies


def interaction():
    """
    Работа консоли с пользователем
    """
    user_input_keyword = input("Введите название профессии для запроса вакансий из hh.ru. Например, programmer \n")
    hh = HH()
    x = hh.load_vacancies(user_input_keyword)
    vacan = Vacancies.get_vacancy_list(x, user_input_keyword)
    if user_input_keyword.isalpha():
        vacan.sort(reverse=True)
    else:
        return "Вы ввели некорректный запрос"

    user_input_top = int(input("Введите количество вакансий (Х) для списка ТОП-Х \n"))
    top_x = vacan[0:user_input_top]
    print(top_x)
    return user_input_keyword
