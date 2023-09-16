import os
import time


def chooeese(my_dict):
    choose = input("Y-повторный ввод || N-вернуться в меню: ")
    if choose == "Y":
        print("\n\n")
        buy_prod(my_dict)
    elif choose == "N":
        print("\n\n")
        menu(my_dict)
    else:
        chooeese(my_dict)


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def description_prod(my_dict):
    print("\nОписание продуктов\n")
    for k, v in my_dict.items():
        print("Наименование изделия: \033[33m{}\033[0m".format(k), "\nМатериал: \033[31m{}\033[0m".format(v[0]),
              "\nВставка: \033[31m{}\033[0m" .format(v[1]), "\n")
    menu(my_dict)


def price_name_prod(my_dict):
    print("\nНаименование - цена\n")
    for k, v in my_dict.items():
        print("Наименование изделия: \033[33m{}\033[0m".format(k), "\nЦена: \033[31m{}$\033[0m".format(v[2]), "\n")
    menu(my_dict)


def quantity_prod(my_dict):
    print("Наименование - количество")
    for k, v in my_dict.items():
        print("Наименование изделия: \033[33m{}\033[0m".format(k))
        print("Количество: \033[31m{}\033[0m".format(v[3]), "\n")
    menu(my_dict)


def information_prod(my_dict):
    print("\nВся информация о продуции\n")
    for k, v in my_dict.items():
        print("Наименование изделия: \033[33m{}\033[0m".format(k), "\nМатериал: \033[31m{}\033[0m".format(v[0]),
              "\nВставка: \033[31m{}\033[0m" .format(v[1]),
              "\nЦена: \033[31m{}$\033[0m".format(v[2]), "\nКоличество: \033[31m{}\033[0m".format(v[3]), "\n")
    menu(my_dict)


def buy_prod(my_dict):
    array_prod = list(my_dict.keys())
    print("\n\nПокупка продукта\n\nНиже приведен список продукции\n\n\033[33m{}\033[0m" .format("\n".join(array_prod)),
          "\n")
    production = input("Введите наименование продукции: ")
    if production in array_prod:
        quantity_list = my_dict.get(production)
        if quantity_list[3] != 0:
            print("Количество продукции в магазине: \033[31m{}\033[0m" .format(quantity_list[3]),
                  "\nЦена за 1 единицу товара: \033[31m{}$\033[0m" .format(quantity_list[2]))
            buy_quantity = input("Введите количество товара для покупки: ")
            if isint(buy_quantity):
                while True:
                    if isint(buy_quantity):
                        buy_quantity = int(buy_quantity)
                        if buy_quantity > quantity_list[3]:
                            print("Такого количество товара нет на складе")
                            buy_quantity = input("Повторите попытку ввода: ")
                        elif buy_quantity < 0:
                            print("Некоректный ввод")
                            buy_quantity = input("Повторите попытку ввода: ")
                        else:
                            price = buy_quantity * quantity_list[2]
                            print("Ваш счет: {}" .format(price))
                            quantity_list[3] = quantity_list[3] - buy_quantity
                            my_dict[production] = quantity_list
                            menu(my_dict)
                    else:
                        buy_quantity = input("Повторите попытку ввода: ")
            else:
                while True:
                    buy_quantity = input("Повторите попытку ввода: ")
                    if isint(buy_quantity):
                        buy_quantity = int(buy_quantity)
                        if buy_quantity > quantity_list[3]:
                            print("Такого количество товара нет на складе")
                        elif buy_quantity < 0:
                            print("Некоректный ввод")
                        else:
                            price = buy_quantity * quantity_list[2]
                            print("Ваш счет: {}" .format(price))
                            quantity_list[3] = quantity_list[3] - buy_quantity
                            my_dict[production] = quantity_list
                            menu(my_dict)
        else:
            print("Данный товар раскуплен!!!\n\n")
            menu(my_dict)
    else:
        print("Данной продукции нет в ассортименте магазина")
        chooeese(my_dict)


def menu(my_dict):
    print("Меню".center(40) .upper(),
          "\n1. Просмотр описания: название – описание"
          "\n2. Просмотр цены: название – цена."
          "\n3. Просмотр количества: название – количество."
          "\n4. Всю информацию."
          "\n5. Покупка"
          "\n6. Выход")
    choose = input("Ваш выбор: ")
    if isint(choose):
        choose = int(choose)
        if choose == 1:
            description_prod(my_dict)
        elif choose == 2:
            price_name_prod(my_dict)
        elif choose == 3:
            quantity_prod(my_dict)
        elif choose == 4:
            information_prod(my_dict)
        elif choose == 5:
            buy_prod(my_dict)
        elif choose == 6:
            exit()
        elif choose > 5 or choose < 1:
            print("НЕВЕРНЫЙ ВЫБОР")
            time.sleep(1.5)
            os.system('clear')
            menu(my_dict)
    else:
        print("НЕВЕРНЫЙ ВВОД")
        time.sleep(1.5)
        os.system('clear')
        menu(my_dict)


def main():
    test_dict = {"Золотое кольцо с 2 бриллиантами": ["золото", "бриллианты", 845.03, 10],
                 "Кольцо из золота с фианитами": ["золото", "фианит", 153.2, 20],
                 "Кольцо из золота с наношпинелью и фианитами": ["золото", "наношпинель / фианит", 329.12, 15],
                 "Серебряная цепочка": ["серебро", "без вставки", 163.23, 30]}
    menu(test_dict)


if __name__ == "__main__":
    main()
