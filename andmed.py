import json                              # нужен для работы с JSON

FAIL = "data.json"                       # файл где храним все данные


def lae_andmed():
    """Lae andmed failist."""            # загрузка данных из файла
    try:
        with open(FAIL, "r", encoding="utf-8") as f:   # открываем файл на чтение
            return json.load(f)          # читаем JSON и превращаем в словарь

    except FileNotFoundError:            # если файла ещё нет
        return {}                        # возвращаем пустой словарь

    except json.JSONDecodeError:         # если файл сломан/пустой
        return {}                        # тоже возвращаем пустое


def salvesta_andmed(andmed):
    """Salvesta andmed faili."""         # сохранение данных в файл
    with open(FAIL, "w", encoding="utf-8") as f:   # открываем файл на запись
        json.dump(andmed, f, indent=4, ensure_ascii=False)  # сохраняем красиво
