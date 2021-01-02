def division_func(number, divider):
    """Выводит на печать выражение деления с ответом.
    Именованные параметры:
    number - делимое
    divider - делитель
    Параметры запрашиваются у пользователя.
    Делитель запрашивается до тех пор, пока не будет введен не 0.
    """
    number = float(input('Введите делимое: '))
    divider = 0
    while divider == 0:
        divider = float(input('Введите делитель (не 0!): '))
    print(f'{number} / {divider} =',round(number/divider, 4))
division_func(number=0, divider=1)