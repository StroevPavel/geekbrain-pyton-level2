# coding: utf-8

"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv()
"""
import re
import csv

def get_data():
	main_data = [['Изготовитель системы','Название ОС','Код продукта','Тип системы'],]
	os_prod_list = []
	os_name_list = []
	os_code_list = []
	os_type_list = []
	i = 1
	while i < 4:
		fname = "csv\info_" + str(i) + ".txt"
		with open(fname) as f_txt:
			for rline in f_txt:
				if re.search(r'Изготовитель системы', rline):
					os_prod_list.append(rline.split(':')[1].strip())
				elif re.search(r'Название ОС', rline):
					os_name_list.append(rline.split(':')[1].strip())
				elif re.search(r'Код продукта', rline):
					os_code_list.append(rline.split(':')[1].strip())
				elif re.search(r'Тип системы', rline):
					os_type_list.append(rline.split(':')[1].strip())
					#print(rline.split(':')[1].strip())
			f_txt.close()
		i += 1

	i = 0
	for os_prod in os_prod_list:
		sub_list = []
		sub_list.append(os_prod)
		sub_list.append(os_name_list[i])
		sub_list.append(os_code_list[i])
		sub_list.append(os_type_list[i])
		main_data.append(sub_list)
		i += 1

	return main_data

def write_to_csv(csv_file):
	with open(csv_file, 'w') as csv_file:
		csv_file_writer = csv.writer(csv_file)
		for row in get_data():
			csv_file_writer.writerow(row)


write_to_csv("csv\data.csv") 