# coding: utf-8

"""
Для всех функций из урока 3 написать тесты с использованием unittest. 
Они должны быть оформлены в отдельных скриптах с префиксом test_ в имени файла 
(например, test_client.py).
"""

import socket
import json
# from datetime import datetime 
import sys
import argparse

#from text import routes
from routes import get_server_routes


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
	print("Client detected {}".format(address))
	data = client.recv(1024) # извлекаем данные из клиентского соединения
	request = json.loads(data.decode('utf-8'))

	# начало - код на самостоятельную оптимизацию
	client_action = request.get('action')
	resolved_routes = list(
		filter(
			lambda itm: itm.get('action') == client_action, 
			get_server_routes()
			)
	)
	route = resolved_routes[0] if resolved_routes else None
	# конец - код на самостоятельную оптимизацию

	if route:
		controller = route.get('controller')
		response_string = controller(request.get('data'))

	else:
		response_string = "Unknown action!"


	client.send(response_string.encode('utf-8')) # отправляем ответ на клиента
	client.close()

"""	
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
		print("Action={} Sended {} to client {} IP={}".format(request.get('action'), dt_str, request.get('client'), address))
		client.close()
	else:
		response_string = "Unknown action!"
		client.send(response_string.encode('utf-8'))
		print("Action={} from client IP={} is unknown!".format(action, address))
		client.close()
"""