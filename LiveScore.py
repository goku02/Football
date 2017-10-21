import argparse
import values

import json
import urllib.request as urlrequest
import urllib.parse as urlparse
from urllib.parse import urlencode

import termgraph

def display_data(data):
	termgraph.chart(
		labels = [d["team_name"] for d in data],
		data = [int(d["overall_league_PTS"]) for d in data],
		args = dict(
			width = 30,
			suffix = "",
			format = "{:>5.0f}"
		)
	)

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

def all_countries():
	url = 'https://apifootball.com/api/?action=get_countries&APIkey=' + values.API_KEY
	with urlrequest.urlopen(url) as r:
		for d in json.loads(r.read()):
			yield d["country_id"]
		#data = json.loads(r.read())
	#return [d["country_id"] for d in data]

def get_leagues_id(country_id):
	url = 'https://apifootball.com/api/?action=get_leagues&country_id=' + country_id + '&APIkey=' + values.API_KEY
	with urlrequest.urlopen(url) as r:
		for d in json.loads(r.read()):
			yield d["league_id"]

def all_leagues(countries_id):
	list_league_id = []
	for c in countries_id:
		url = 'https://apifootball.com/api/?action=get_leagues&country_id=' + c + '&APIkey=' + values.API_KEY
		with urlrequest.urlopen(url) as r:
			data = json.loads(r.read())
			list_league_id.append += [d["league_id"] for d in data]

	return list_league_id

def main():
	for c in all_countries():
		print(c)
		for l in get_leagues_id(c):
			print(l, end=' ')
		print()

	all_countries_id = all_countries()
	print(all_countries_id)
	
	#all_leagues_id = all_leagues(all_countries_id)
	#print(all_leagues_id)

	parser = argparse.ArgumentParser(description='Get Football News')
	parser.add_argument('action', help="What type of data is to be fetched", choices=values.actions)
	#args = parser.parse_args()
	#get_url(args)
	parser.add_argument('-c', '--country_id', help="The identifier of the country whose leagues will be fetched.", type=int, choices=all_countries_id)
	parser.add_argument('-l', '--league_id', help="The identifier of the league whose standings will be fetched.", type=int)
	args = parser.parse_args()
	url = get_url(args)
	print(url)
	#print(args.country_id)
	#print(args.league_id)
	with urlrequest.urlopen(url) as r:
		data = json.loads(r.read())
		#print(data)
		data = sorted(data, key=lambda data: int(data['overall_league_position']))
		# for d in data:
		# 	print(d)
		# 	print()

	print()
	print("==========================================================================\n")
	print("League === {0}".format(data[0]["league_name"]))
	display_data(data)


def getData():
	url = 'https://apifootball.com/api/?action=get_countries&APIkey=' + values.API_KEY
	with urlrequest.urlopen(url) as r:
		data = json.loads(r.read())
		for d in data:
			print(d)

if __name__ == "__main__":
	main()
	