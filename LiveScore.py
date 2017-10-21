import argparse
import values

import json
import urllib.request as urlrequest
import urllib.parse as urlparse
from urllib.parse import urlencode

def get_url(args):
	'''
	Prepares the URL from which the data will be fetched based on the command line arguments.
	'''
	#print(args)
	params = {}
	#print(url_parts)

	for arg in vars(args):
		#print(arg, getattr(args, arg))
		if getattr(args, arg) is not None:
			params.update({arg: getattr(args, arg)})
	params.update({'APIkey': values.API_KEY})

	url = values.API_URL
	url_parts = list(urlparse.urlparse(url))
	#print(params)
	query = dict(urlparse.parse_qsl(url_parts[4]))
	query.update(params)
	#print(query)
	url_parts[4] = urlencode(query)

	#print(urlparse.urlunparse(url_parts))
	#print('URL => {0}'.format(url))
	return urlparse.urlunparse(url_parts)

def main():
	parser = argparse.ArgumentParser(description='Get Football News')
	parser.add_argument('action', help="What type of data is to be fetched", choices=values.actions)
	#args = parser.parse_args()
	#get_url(args)
	parser.add_argument('-c', '--country_id', help="The identifier of the country whose leagues will be fetched.", type=int)
	parser.add_argument('-l', '--league_id', help="The identifier of the league whose standings will be fetched.", type=int)
	args = parser.parse_args()
	url = get_url(args)
	print(url)
	with urlrequest.urlopen(url) as r:
		data = json.loads(r.read())
		#print(data)

		data = sorted(data, key=lambda data: int(data['overall_league_position']))
		for d in data:
			print(d)
			print()

def getData():
	url = 'https://apifootball.com/api/?action=get_countries&APIkey=' + values.API_KEY
	with urlrequest.urlopen(url) as r:
		data = json.loads(r.read())
		for d in data:
			print(d)

if __name__ == "__main__":
	main()
	