from pycricbuzz import Cricbuzz
from pprint import pprint

c = Cricbuzz()
matches = c.matches()

home = raw_input("Enter home team: ")
away = raw_input("Enter away team: ")

player1 = raw_input("Enter first player: ")
# player2 = raw_input("Enter secoind player: ")
# player3 = raw_input("Enter third player: ")

for match in matches:
    if(match['srs'] == 'Indian Premier League 2019' and match['team1']['name'] == home and match['team2']['name'] == away):
        pprint(match)
        pprint(c.scorecard(match['id']))
	#if(match['mchstate'] != 'nextlive'):
		#pprint(c.livescore(match['id']))
		#print c.commentary(match['id'])
		#print c.scorecard(match['id'])
