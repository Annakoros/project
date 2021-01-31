#3. Создайте собственный класс-исключение, который должен проверять содержимое списка
# на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
class Check_Value:

    def __init__(self):
        inp = ''
        inp_list = []

    def list_maker(self):
        inp = ''
        inp_list = []
        while inp != 'stop':
            inp = input('Введите число в список (для завершения введите "stop"): ')
            try:
                inp_list.append(int(inp))
            except ValueError:
                if inp != 'stop':
                    print('Вы ввели не число')
        return inp_list

my_list = Check_Value()
print(f'Сформирован список чисел: {my_list.list_maker()}')
