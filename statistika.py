def kuva_statistika(harjumused):
    text = "Statistika:\n\n"             # заголовок статистики

    clean_data = {}                      # сюда складываем только нормальные данные

    for nimi, kogus in harjumused.items():   # перебираем все привычки
        if isinstance(kogus, (int, float)):  # проверяем что значение число
            clean_data[nimi] = kogus         # оставляем как есть
        else:
            clean_data[nimi] = 0             # если нет — ставим 0

    sorted_harjumused = sorted(              # сортируем привычки
        clean_data.items(),
        key=lambda x: x[1],                  # сортировка по количеству
        reverse=True                         # от большего к меньшему
    )

    for nimi, kogus in sorted_harjumused:    # собираем красивый текст
        text += f" - {nimi}: {kogus}\n"

    return text                              # возвращаем готовую статистику
