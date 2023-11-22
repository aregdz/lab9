#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    print("Список команд:\n")
    print("add - добавить рейс;")
    print("list - вывести список рйсов;")
    print("select <тип> - вывод на экран пунктов назначения и номеров рейсов для данного типа самолёта")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")

    # Список работников.
    aircrafts = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        
        # Выполнить действие в соответствие с командой.
        match comand:
            case 'exit':
                break

            case 'add':
            # Запросить данные о работнике.
                name = input("Название пункта назначения рейса? ")
                number = int(input("Номер рейса? "))
                tip = input("Тип самолета? ")

                # Создать словарь.
                i = {'name': name, 'number': number, 'tip': tip}

                # Добавить словарь в список.
                aircrafts.append(i)

                # Отсортировать список в случае необходимости.
                if len(aircrafts) > 1:
                    aircrafts.sort(key=lambda item: item.get('name', ''))

            case 'list':
                # Заголовок таблицы.
                line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
                )
                print(line)

                # Вывести данные о всех сотрудниках.
                for idx, i in enumerate(aircrafts, 1):
                    print(
                        '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                            idx,
                            i.get('name', ''),
                            i.get('number', ''),
                            i.get('tip', '')
                        )
                )
                print(line)

            case 'select ':
                # Разбить команду на части для выделения номера года.
                parts = input("Введите значение: ")

                # Проверить сведения работников из списка.
                count = 0
                for i in aircrafts:
                    for k, v in i.items():
                        if v == parts:
                            print("Пункт назначения - ", i["name"])
                            print("Номер рейса - ", i["number"])
                            count += 1

                # Если счетчик равен 0, то работники не найдены.
                if count == 0:
                    print("Рейс с заданным типом самолёта не найден.")

            case 'help':
                # Вывести справку о работе с программой.
                print("Список команд:\n")
                print("add - добавить рейс;")
                print("list - вывести список рйсов;")
                print("select <тип> - вывод на экран пунктов назначения и номеров рейсов для данного типа самолёта")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")

            case _:
                print(f"Неизвестная команда {command}")
