from logger import input_data, print_data, copy_data, delete_data, modify_data


def interface():
    while True:
        print('Добрый день! Это бот-помощник. \n'
          'Что вы хотите сделать? \n'
          '1 - Записать данные \n'
          '2 - Вывести данные \n'
          '3 - Скопировать данные из файла \n'
          '4 - Удалить данные из файла \n'
          '5 - Изменить данные в файле \n'
          '6 - Выйти из программы')
        command = int(input('Ваш выбор: '))

        while command < 1 or command > 6:
            command = int(input('Ошибка! Ваш выбор: '))

        if command == 1:
            input_data()
        elif command == 2:
            print_data()
        elif command == 3:
            index = int(input("Введите номер данных, которые нужно скопировать: "))
            copy_data(index)
        elif command == 4:
            index = int(input("Введите номер данных, которые нужно удалить: "))
            delete_data(index)
        elif command == 5:
            index = int(input("Введите номер данных, которые нужно изменить: "))
            new_data = input("Введите новые данные: ")
            modify_data(index, new_data)
        elif command == 6:
            break

interface()
