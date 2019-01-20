# coding: utf-8

import os
import sys
import psutil
import shutil

answer = '' 			# Задаем пустую переменную для цикла while
fragment = '.dupl'		# назначаем фрагмент имени, который будет добавляться или искаться

print("Старт программы")
name = input("Введите логин: ")
print('Привествую {}!'.format(name))

while answer != 'q':
	answer = input("Продолжить выполнение программы?(y/n/ q - для завершения) ")
	if answer == "y":
		print("Продолжаем работать. Что делаем?")
		print("	[1] - Вывести список содержимого текущей папки.")
		print("	[2] - Вывести информацию о системе")
		print("	[3] - Вывести список запущенных процессов в системе")
		print("	[4] - Вывести Информацию о процессоре")
		print("	[5] - Дублирование файлов в текущей папке")	
		print("	[6] - Дубливароние указанного файла")	
		print("	[7] - Удаление всех бэкапов")	
			
		do = input("Выберете номер строки [1-7]: ")
		if not do.isdigit():
			print("Вы ввели не числовое значение. Повторите.")
			continue
		do = int(do)
		if do == 1:
			print('Содержимое текущей директории: ', os.listdir())
		elif do == 2:
			print("Платформа: ", sys.platform, "\nСистема: ", os.name)
			print("Пользователь: ", os.getlogin())
			print("Кодировка по-умолчанию: ", sys.getdefaultencoding())
		elif do == 3:
			print("ID всех запущенный процессов: ", psutil.pids())
		elif do == 4:
			print("Кол-во ядер Процессора: ", psutil.cpu_count())
		
		elif do == 5:
			print("Дублирование всех файлов в папке")
			file_list = os.listdir()
			for oldf in file_list:
				if os.path.isfile(oldf):
					newfile = oldf + '.dupl'
					shutil.copy(oldf, newfile)
					if os.path.exists(newfile):
						print("Создан файл: {}.".format(newfile))
			print("Окончание копирования всех файлов в директории. Перезагрузка")
		elif do == 6:
			print("Дублирование указанного файла")
			filename = input('Введите имя файла: ')
			if os.path.isfile(filename):
				newfile = filename + '.dupl'
				shutil.copy(filename, newfile)
				if os.path.exists(newfile):
					print("Создан файл: {}. Перезагрузка.".format(newfile))
			else:
				print('Вы ввели имя папки, а не файла. Повторите!')
				continue
							
		elif do == 7:
			print("Режим удаления дубликатов в выбранной директории: ")
			dirname = input('Укажите имя директории.\nДля текущей директроии укажите " . ": ')
			file_list = os.listdir(dirname)
			for f in file_list:
				fullname = os.path.join(dirname, f)  # \ - разделитель в win, / - разд.в unix
				if fullname.endswith('.dupl'):
					os.remove(fullname)
					print("Удален файл: " + fullname)
			print("Завершение функции удаления. Перезагрузка")
		else:
			print("Ошибка ввода номера строки")
			
	elif answer == "n":
		print("Перезапуск программы")
	elif answer == "q":
		print("Завершение работы программы")
	else:
		print("Некорректный ответ")
