from datetime import datetime 

def get_date_time():
	dt = datetime.now()
	dt_str = dt.strftime('%d-%m-%yT%H:%M:%S')
	return json.dumps(
		{
		'action': request.get('action'),
		'client': address,
		'datetime': dt_str
		}