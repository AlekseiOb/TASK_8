from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные? \n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')


def print_data():
    print('1 файл:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        for index, row in enumerate(data, start=1):
            if row.strip():
                print(f'{index}: {row.strip()}')

    print('2 файл:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        for index, row in enumerate(data, start=1):
            if row.strip():
                fields = row.strip().split(';')
                print(f'{index}: {"; ".join(fields)}')

def copy_data(index):
    with open('data_first_variant2.csv', 'r') as file:
        data = file.readlines()
        if 0 < index <= len(data):
            with open('data_first_variant.csv', 'a') as f_dest:
                f_dest.write(data[index - 1])
        else:
            print("Ошибка: таких данных нет.")
    
def delete_data(index):
    with open('data_first_variant.csv', 'r') as file:
        data = file.readlines()
        if 0 < index <= len(data):
            del data[index - 1]
            with open('data_first_variant.csv', 'w') as file:
                file.writelines(data)
        else:
            print("Ошибка: таких данных нет.")


def modify_data(index, new_data):
    with open('data_first_variant.csv', 'r') as file:
        data = file.readlines()
        if 0 < index <= len(data):
            data[index - 1] = new_data + '\n'
            with open('data_first_variant.csv', 'w') as file:
                file.writelines(data)
        else:
            print("Ошибка: Таких данных нет.")