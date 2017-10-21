API_KEY = ''
# https://apifootball.com/api/?action=get_leagues&country_id=169&APIkey=

actions = ["get_countries", "get_leagues", "get_standings", "get_events"]

API_URL = 'https://apifootball.com/api/?'

'''
Parameters => action, API Key
'''
GET_COUNTRIES_URL = 'https://apifootball.com/api/?action=get_countries&APIkey='

'''
Parameters => action, country id, API Key
Competitions  =>  https://apifootball.com/api/?action=get_leagues&country_id=169&APIkey=xxxxxxxxxxxxxx
'''
COMPETITIONS_URL = 'https://apifootball.com/api/?action=get_leagues&country_id=169&APIkey=xxxxxxxxxxxxxx'

'''
Parameters => action, league id PAI Key
Standings  =>  https://apifootball.com/api/?action=get_standings&league_id=62&APIkey=xxxxxxxxxxxxxx
STANDINGS_URL = 'https://apifootball.com/api/?action=get_standings&league_id=62&APIkey=xxxxxxxxxxxxxx'
'''

'''
Parameters => action, from, to, league id, API Key
Events(Results/Fixtures)
https://apifootball.com/api/?action=get_events&from=2016-10-30&to=2016-11-01&league_id=62&APIkey=xxxxxxxxxxxxxx
'''
EVENTS_URL = 'https://apifootball.com/api/?action=get_events&from=2016-10-30&to=2016-11-01&league_id=62&APIkey=xxxxxxxxxxxxxx'