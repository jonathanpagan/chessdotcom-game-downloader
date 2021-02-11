import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import re
from numpy import savetxt

def clean_pgn(pgn):
    """deletes clock times from pgn string"""
    return(re.sub(r'\ {.*?\}', '', pgn))
    
def fetch(username):
    """retrieves all of the standard chess games from the username account 
    using beautifulsoup and json to parse the games from chess.com's API. 
    returns a DataFrame where each row represents a single game."""
    
    url = f'https://api.chess.com/pub/player/{username}/games/archives'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    months = json.loads(soup.prettify())['archives']
    l = []
    
    for month in months:
        archive = BeautifulSoup(requests.get(month).content, 'html.parser').prettify()
        l.extend(json.loads(archive)['games'])

    df = pd.DataFrame(l).query('rules == "chess"')
    df['pgn'] = df['pgn'].map(clean_pgn)
    
    return(df)

def main():
    username = input(r'Whose games would you like to download from chess.com? ')
    output = fetch(username)
    with open(fr'{username}.pgn', 'a', encoding='utf-8') as f:
        if len(output) != 0:
            savetxt(f, output['pgn'].values, fmt='%s')

if __name__ == '__main__':
    main()