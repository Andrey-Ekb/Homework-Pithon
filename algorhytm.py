from functional import create
from interface import interface
path = "phone_book.txt"
create(path)
enter = 0
print()
while enter != 6:
    enter = interface()
    if enter == 1:
        from functional import add_cont 
        print()
        stroka = str(input("Введите ФИО и номер телефона через пробел "))
        add_cont(path, stroka)
    elif enter == 2:
        from functional import show_all
        print(show_all(path))
    elif enter == 3:
        from functional import search
        stroka = str(input("Введите фамилию "))
        search(path, stroka)
    elif enter == 4:
        from functional import del_cont
        print()
        stroka = str(input("Введите ФИО для удаления - "))
        del_cont(path, stroka)    
    elif enter == 5:
        from functional import change_cont
        print()
        stroka = str(input("Введите искомую ФИО - "))
        change_cont(path, stroka)
print()
print("спасибо за работу")
print()
