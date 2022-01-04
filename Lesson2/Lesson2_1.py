1.# Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов 
#info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
#Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
#В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель
#системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список. 
#Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции 
#создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета  
#в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также 
#оформить в виде списка и поместить в файл main_data (также для каждого файла);
#Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных 
#через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
#Проверить работу программы через вызов функции write_to_csv().
import re
import csv

def get_data(us_l):
	main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
	os_prod_list = []
	os_name_list = []
	os_code_list = []
	os_type_list = []

	for data_r in us_l:
		file_dat = open(data_r)
		for row in file_dat:
			row = row.rstrip()
			if re.match('Изготовитель системы', row):
				os_prod_list.append(re.search(r'(Изготовитель системы).\s*(.*)', row).group(2))
			elif re.match('Название ОС', row):
				os_name_list.append(re.search(r'(Название ОС).\s*(.*)', row).group(2))
			elif  re.match('Код продукта', row):
				os_code_list.append(re.search(r'(Код продукта).\s*(.*)', row).group(2))
			elif  re.match('Тип системы', row):
				os_type_list.append(re.search(r'(Тип системы).\s*(.*)', row).group(2))

	for i in range(len(us_l)):
		main_data.append([
			os_prod_list[i],
			os_name_list[i],
			os_code_list[i],
			os_type_list[i]
			])

	return main_data

def csv_write(file, words):
	with open(file, 'w') as f_n:
		f_n_data = csv.writer(f_n)
		for a in words:
			f_n_data.writerow(a)


test = get_data(['info_1.txt', 'info_2.txt', 'info_3.txt'])
csv_write('my_test.csv', test)

with open('my_test.csv', 'r') as f_n:
	print(f_n.read())
