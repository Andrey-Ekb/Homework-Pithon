"""

# 55.  Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Поиск по фамилии
from func import *


privet()

# 1 - Интерфейс
# 2 - работа с файлом
# 3 - алгоритм


# 1 - добавление контакта
# 2 - вывод всех
# 3 - поиск по фамилии
# 4 - удаление контакта
# 5 - редактирование контакта
# 4 - выход

"""
def create(path):
    try:
        file = open(path, 'r')
    except IOError:
        print('Создан новый справочник -> phone_book.txt ')
        file = open(path, 'w')
    finally:
        file.close()

def add_cont(file_name, stroka):
    data = open(file_name, 'a')
    data.write(stroka + "\n")
    data.close()

def show_all(file_name):
    data = open(file_name, "r")
    for line in data:
        print(line[:-1])
    data.close()

def search(file_name, stroka):
    a = 0
    data = open(file_name, 'r')
    for line in data:
        if stroka in line:
            print(line)
            a = 123
            break
    if a != 123:
        print("нет такого")
    data.close()
    
def del_cont(file_name, stroka):
    data = open(file_name,'r')
    list_name= list()
    for line in data:
        if stroka in line:
            print_name = line
            continue
        if line !='':
            list_name.append(line)
    data.close()
    
    list_name=list(filter(lambda x: x !='', list_name))
    data=open(file_name,'w')
    for item in list_name:
        data.write(item)
    data.close()
    print((f'Контакт: { stroka } удален \n'))

def change_cont(file_name, stroka):
    data = open(file_name,'r')
    list_name= list()
    for line in data:
        if stroka in line:
            new_name = input('Введите данные с изменением ')
            list_name.append(new_name +"\n")
            continue
        list_name.append(line)
    data.close()
    
    list_name=list(filter(lambda x: x !='', list_name))
    data=open(file_name,'w')
    for item in list_name:
        data.write(item)
    data.close()
    print()