from datetime import datetime 
import json

def get_date_time(data):
	dt = datetime.now()
	return json.dumps(
		{
		'action': 'get_time',
		'datetime': dt.strftime('%d-%m-%yT%H:%M:%S')
		}
	)