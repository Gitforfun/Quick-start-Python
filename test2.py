# coding: utf-8
#def find(target, s_list):
#	return target in s_list, \
#		[name for name in s_list if (target in name or name in target) and abs(len(name) - len(target))<= 3] if target not in s_list else None
import os

file_list = os.listdir()	# получаем список
fragment = '.dupl'			# назначаем фрагмент имени, которое будет искать
del_file_list = []			# создаем новый список, в который будем вносить все найденные подобные имена
for element in file_list:	# для каждого элемента (для них создали новую переменную) списка файлов:
	if (fragment in element):	# если искомый фрагмент есть в элементе списка или элемент списка есть в искомом фрагменте
		del_file_list.append(element)# заносим найденный элемент в новый список
print (del_file_list)		# выводим новый список для проверки




#		print ('подобные: "{}"!'.format(element)) # красивый вывод информации
