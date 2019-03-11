# coding: utf-8

"""
Функции сервера: принимает сообщение клиента; формирует ответ клиенту; 
отправляет ответ клиенту; имеет параметры командной строки: 
-p <port> — TCP-порт для работы (по умолчанию использует 7777); 
-a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса)
"""

import socket
import json
from datetime import datetime 
import sys
import argparse

def createParser(): # парсер для командной строки
	parser = argparse.ArgumentParser()
	parser.add_argument ('-a', default='localhost')
	parser.add_argument ('-p', default='7777')
	return parser

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])

sock = socket.socket()
sock.bind((namespace.a, int(namespace.p)))
sock.listen(5) # сколько одновременных соединений поддерживаем

print("Server started on IP={} and port={}".format(namespace.a, namespace.p))

while True: # бесконечный цикл для чтения данных от клиентов
	client, address = sock.accept()
	print('Client detected {address}')
	data = client.recv(1024) # извлекаем данные из клиентского соединения
	request = json.loads(data.decode('utf-8'))
	
	if request.get('action') == 'get_time':
		dt = datetime.now()
		dt_str = dt.strftime('%d-%m-%yT%H:%M:%S')
		response_string = json.dumps(
			{
			'action': request.get('action'),
			'client': address,
			'datetime': dt_str
			}
		)
		client.send(response_string.encode('utf-8')) # отправляем ответ на клиента
		print("Action={} Sended {} to client IP={}".format(request.get('action'), dt_str, address))
		client.close()
	else:
		response_string = "Unknown action!"
		client.send(response_string.encode('utf-8'))
		print("Action={} from client IP={} is unknown!".format(action, address))
		client.close()