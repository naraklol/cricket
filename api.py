from pycricbuzz import Cricbuzz
from pprint import pprint

class Player():
    def __init__(self, name):
        self.name = name
        self.batruns = 0
        self.batballs = 0
        self.bowlruns = 0
        self.wickets = 0
        self.overs = 0
        self.catches = 0
        self.runouts = 0
        self.dismissal = ""

        self.found = False

    def printStats(self):
        if self.found:
            print 'Name - ' + str(self.name)
            print 'BatRuns - ' + str(self.batruns)
            print 'BatBalls - ' + str(self.batballs)
            print 'Dismissal - ' + self.dismissal
            print 'BowlRuns - ' + str(self.bowlruns)
            print 'Wickets - ' + str(self.wickets)
            print 'Overs - ' + str(self.overs)
            print 'Catches - ' + str(self.catches)
            print 'Run Outs - ' + str(self.runouts)
            print ''

    def getStats(self):
        for match in matches:
            if(match['srs'] == 'Indian Premier League 2019' and match['team1']['name'] == home and match['team2']['name'] == away):
                for inning in c.scorecard(match['id'])['scorecard']:
                        for batter in inning['batcard']:
                            if batter['name'] == self.name:
                                self.found = True
                                self.batruns = float(batter['runs'])
                                self.batballs = float(batter['balls'])
                                self.dismissal = batter['dismissal']
                            self.extras(batter['dismissal'])
                        for bowler in inning['bowlcard']:
                            if bowler['name'] == self.name:
                                self.found = True
                                self.bowlruns = float(bowler['runs'])
                                self.overs = float(bowler['overs'])
                                self.wickets = float(bowler['wickets'])

    def extras(self, cause):
        catch = cause.split()
        if catch[0] == 'c' and (catch[1] == self.name.split()[0] or catch[2] == self.name.split()[0]):
            self.catches += 1

        ro = cause.split('(')
        if ro[0] == 'run out ' and ro[1].split(')')[0] == self.name:
            self.runouts += 1

    def score(self):
        score = float(0)
        if self.overs != 0:
            econ = self.bowlruns/self.overs
        else:
            econ = 0
        score += self.batruns
        if self.batballs >= 10:
            score += ((self.batruns/self.batballs) * float(100))/float(10) * float(1.5)
        if econ <= 10 and econ > 0:
            score += float(100)/econ * float(1.5)
        score += self.wickets * 20
        score += self.catches * 15
        score += self.runouts * 15
        return score

team = {}
team['MI'] = 'Mumbai Indians'
team['CSK'] = 'Chennai Super Kings'
team['DC'] = 'Delhi Capitals'
team['KKR'] = 'Kolkata Knight Riders'
team['KXIP'] = 'Kings XI Punjab'
team['RCB'] = 'Royal Challengers Bangalore'
team['RR'] = 'Rajasthan Royals'
team['SRH'] = 'Sunrisers Hyderabad'


c = Cricbuzz()
matches = c.matches()
home = ''
away = ''

players = []

def input():
    global home
    global away

    home = team[raw_input('Enter home team: ')]
    away = team[raw_input('Enter away team: ')]

    while True:
        player = Player(raw_input("Enter first player: "))
        if playerCheck(player):
            break
    while True:
        player = Player(raw_input("Enter second player: "))
        if playerCheck(player):
            break
    while True:
        player = Player(raw_input("Enter third player: "))
        if playerCheck(player):
            break

def playerCheck(player):
    player.getStats()
    if player.found == True:
        players.append(player)
        return True
    else:
        print 'Player not found'
        return False


input()
total = 0
for player in players:
    player.printStats()
    total += player.score()
    print 'Score = ' + str(player.score()) + '\n'

print 'Total score = ' + str(total) + '\n'
