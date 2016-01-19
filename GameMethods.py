from Game import *

def BuildGameObject(event):
    away = event['performers'][1]['name']
    home = event['performers'][0]['name']
    date = event['datetime_local'][0:event['datetime_local'].index('T')]
    score = event['stats']['lowest_price_good_deals']

    return Game(away, home, date, score)

def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1
