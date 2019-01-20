# coding: utf-8

import os
import sys
import psutil

answer = ''  # Задаем пустую переменную для цикла while

print("New working program")
name = input ("Ваше имя: ")
print("Привествую,", name)
while answer != 'Q':

    answer = input ("Продолжить запуск программы?(Y/N/ Q - для завершения)")
    if (answer == "Y"):
        print ("Продолжаем работать. Что делаем?")
        print("	[1] - Вывести список содержимого текущей папки.")
        print("	[2] - Вывести информацию о системе")
        print("	[3] - Вывести список запущенных процессов в системе")
        print("	[4] - Вывести Информацию о процессоре")

        do = int(input ("Выберете номер строки [1-5]:"))

        if (do == 1):
            print ("Содержимое текущей директории: ", os.listdir())
        elif (do == 2):
            print ("Платформа: ", sys.platform, "\nСистема: ", os.name)
            print ("Пользователь: ", os.getlogin())
            print ("Кодировка по-умолчанию: ", sys.getdefaultencoding() )
        elif (do == 3):
            print ("ID всех запущенный процессов: ", psutil.pids())
        elif (do == 4):
            print ("Кол-во ядер Процессора: ", psutil.cpu_count())
        else:
            print ("Ошибка ввода номера строки")

    elif (answer == "N"):
        print ("Выход из программы")
    else:
        print ("Некорректный ответ")
