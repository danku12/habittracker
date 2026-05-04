class Harjumus:                           # класс для одной привычки
    """Klass harjumuse koguse jälgimiseks (nt ml, km jne)."""

    def __init__(self, nimi: str):        # создаётся новая привычка
        self.nimi = nimi                  # сохраняем название
        self.kogus = 0                    # стартовое значение всегда 0

    def lisa_kogus(self, amount: int):    # добавляем прогресс
        self.kogus += amount              # прибавляем новое значение

    def saa_kogus(self) -> int:           # получить текщее количество
        return self.kogus                 # возвращаем прогресс