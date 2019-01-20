# coding: utf-8
# Комментарии
import os
import sys
import psutil
import shutil

answer ='' # Задаем пустую переменную для цикла while

print ("New working program")
name = input ("Ваше имя: ")
print ("Привествую,", name)
while answer !='q':
	
	answer = input ("Продолжить выполнение программы?(y/n/ q - для завершения)")
	if (answer == "y"):
		print ("Продолжаем работать. Что делаем?")
		print("	[1] - Вывести список содержимого текущей папки.")
		print("	[2] - Вывести информацию о системе")
		print("	[3] - Вывести список запущенных процессов в системе")
		print("	[4] - Вывести Информацию о процессоре")
		print("	[5] - Дублирование выбранного файла")	
		print("	[6] - Удаление выбранного файла")	
			
		do = int(input ("Выберете номер строки [1-6]:"))
		
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
		
		elif (do == 5):
			print ("Вывод файлов в директории: ")
			file_list = os.listdir()
			for i in range (0, len(file_list)):
				print ("	", i+1, ".	", file_list[i])
			i = int(input("Выберете номер файла для копирования: "))	
			print ("Выбран файл: ",file_list[i-1])
			new_name = input("Введите новое имя выбранного файла: ")	
			shutil.copy2(file_list[i-1], new_name)
			print ("Файл ", file_list[i-1], "скопирован с именем ", new_name)	
			file_list = os.listdir()
			print ("Теперь список файлов в текущей директории: ")
			for i in range (0, len(file_list)):
				print ("	", i+1, ".	", file_list[i])
				
		elif (do == 6):
			print ("Вывод файлов в директории: ")
			file_list = os.listdir()
			for i in range (0, len(file_list)):
				print ("	", i+1, ".	", file_list[i])
			i = int(input("Выберете номер файла для удаления: "))	
			print (name, ", Вы выбрали файл: ",file_list[i-1], ",\n	Уверены, что хотите его удалить? [y/n]")		
			alert = input ("Удалить? ")	
			if alert == 'y':
				print("Удален файл: ", file_list[i-1])
				os.remove(file_list[i-1])
				print ("Теперь список файлов в текущей директории: ")
				file_list = os.listdir()
				for i in range (0, len(file_list)):
					print ("	", i+1, ".	", file_list[i])
			elif alert == 'n':
				print("Выход из режима удаления")
		
		else:
			print ("Ошибка ввода номера строки")
			
	elif (answer == "n"):
		print ("Перезапуск программы")
	elif (answer == "q"):
		print ("Завершение работы программы")
	else:
		print ("Некорректный ответ")
