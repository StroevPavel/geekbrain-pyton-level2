# coding: utf-8

"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import pyyaml


yaml_data_to_write = {
	'List_Params': ['list_val1', 'list_val2', 'list_val2'],
	'Integer_Params': 4267,
	'Dict_params': {
		'1€': 'dict_val1',
		'2€': 'dict_val3',
		'3€': 'dict_val3'
	}
}

with open('yaml/file.yaml', 'w') as yaml_file:
    yaml.dump(yaml_data_to_write, yaml_file, default_flow_style=False, allow_unicode = True)

with open('yaml/file.yaml') as yaml_file:
    print(yaml_file.read())