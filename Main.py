from Game import *
from GameMethods import *
import json
import urllib2
import random
     
def Main():
    games = []
    allTeams = ['http://api.seatgeek.com/2/events?performers[home_team].id=9&per_page=25',
                'http://api.seatgeek.com/2/events?performers[home_team].id=8&per_page=25']
    
    
    for team in allTeams:
        response = urllib2.urlopen(team)
        html = response.read()
        jsonData = json.loads(html)
        
        for event in jsonData['events']:
            if (find_str(event['title'], 'Spring') == -1): #Dont want Spring Training Games
                g = BuildGameObject(event)
                games.append(g)

    games.sort(key=lambda x: x.bestScore, reverse=True)
    
    for g in games:
        print str(g.bestScore) + ": " + g.awayTeam + " @ " + g.homeTeam + " " + g.date
                
    
Main()
