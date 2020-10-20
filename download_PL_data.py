import requests
import pandas as pd
import os


initial_season = 8485
year = initial_season

#Download and save data previous to season 2018/2019

while season != 1819:    
    season = season + 101 #The PL season is reported in the file name as a 4 digits number (e.g: 2003/2004 is 0304); to move from one season to the following
    if (season==10000):   # we can add 101 (e.g.: 0304 + 101 -> 0405). The only exception is the roll over at the end of the century: 9899 + 101 -> 10000
        season = 1        # For this reason when the loop gets to season 2000-2001 the season variable is reset to 0001. 
    season_4_digits = str(season).zfill(4) # adds zeros before the actual number (needed for seasons between 2000-2001 and 2009-2010
    csv_url = string = 'https://www.football-data.co.uk/mmz4281/'+ season_4_digits + '/E0.csv'
    req = requests.get(csv_url)
    if req.status_code == 200:
        url_content = req.content
        output_file_name = 'PL' + season_4_digits + '.csv'

        output_file = open(output_file_name, 'wb')
        output_file.write(url_content)
        output_file.close()
    else:
        continue

#Loop through data downloaded to compute the average percentage of home wins

directory = '.'

total_home_wins=0
total_home_games=0

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        data = pd.read_csv(filename, error_bad_lines=False)
        games_reds_home = len(data[data["HomeTeam"] == 'Liverpool'])
        total_home_games = total_home_games + games_reds_home
        wins_reds_home = len(data[(data["HomeTeam"] == 'Liverpool') & (data['FTR'] == 'H')])
        total_home_wins = total_home_wins + wins_reds_home
        ratio_home_wins = wins_reds_home / games_reds_home

print('Average ratio wins/games: ',total_home_wins/total_home_games)
