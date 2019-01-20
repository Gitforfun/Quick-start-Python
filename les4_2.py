# coding: utf-8

import os
import sys
import psutil
import shutil

answer ='' 			# Задаем пустую переменную для цикла while
fragment = '.dupl'	# назначаем фрагмент имени, который будет добавляться или искаться	

print ("New working program")
name = input ("Ваше имя: ")
print ('Привествую {}!'.format(name))

while answer !='q':
	answer = input ("Продолжить выполнение программы?(y/n/ q - для завершения)")
	if (answer == "y"):
		print("Продолжаем работать. Что делаем?")
		print("	[1] - Вывести список содержимого текущей папки.")
		print("	[2] - Вывести информацию о системе")
		print("	[3] - Вывести список запущенных процессов в системе")
		print("	[4] - Вывести Информацию о процессоре")
		print("	[5] - Бэкап выбранного файла в папку")	
		print("	[6] - Удаление всех бэкапов")	
			
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
			i = int(input("Выберете номер файла для бекапа: "))	
			print (os.path.isfile(file_list[i-1]))
			while (os.path.isfile(file_list[i-1]))!= True:						# П
				print ("Выбран файл: ",file_list[i-1])
				shutil.copy2(file_list[i-1], file_list[i-1]+fragment)
				print ("Создан бэкап для файла:", file_list[i-1], " с именем ", (file_list[i-1]+fragment))	
				file_list = os.listdir()
				print ("Теперь список файлов в текущей директории: ")
				for i in range (0, len(file_list)):
					print ("	", i+1, ".	", file_list[i])
			
			
			
#			if os.path.isfile(file_list[i-1]):							# Проверка выбора файла и не папки
#				print ("Выбран файл: ",file_list[i-1])
#				shutil.copy2(file_list[i-1], file_list[i-1]+fragment)
#				print ("Создан бэкап для файла:", file_list[i-1], " с именем ", (file_list[i-1]+fragment))	
#				file_list = os.listdir()
#				print ("Теперь список файлов в текущей директории: ")
#				for i in range (0, len(file_list)):
#					print ("	", i+1, ".	", file_list[i])
#			else:
#				print (file_list[i-1], ' - является каталогом, а не папкой.')
				
				
				
				
				
		elif (do == 6):
			print ("Режим удаления бекапа. Вывод файлов в директории: ")
			file_list = os.listdir()
			for i in range (0, len(file_list)):
				print ("	", i+1, ".	", file_list[i])
			print ('!!!{}, Вы уверены, что хотите удалить все бэкапы? [y/n]'.format(name))		
			del_file_list = []			# создаем новый список, в который будем вносить все найденные подобные имена
			for element in file_list:	# для каждого элемента (для них создали новую переменную) списка файлов:
				if (fragment in element):	# если искомый фрагмент есть в элементе списка или элемент списка есть в искомом фрагменте
					del_file_list.append(element)# заносим найденный элемент в новый список
			for i in range (0, len(del_file_list)):
				print ("	", i+1, ".	", del_file_list[i])	# выводим список для удаления
			alert = input ("!!!Удалить? ")	
			if alert == 'y':
				for i in range (0, len(del_file_list)):
					os.remove(del_file_list[i])
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
