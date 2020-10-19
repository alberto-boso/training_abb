import requests
import pandas as pd
import os

initial_year = 8485
year = initial_year

#Download and save data previous to season 2018/2019

while year != 1819:
    year = year + 101
    if (year==10000):
        year = 1
    a = str(year).zfill(4)
    csv_url = string = 'https://www.football-data.co.uk/mmz4281/'+ a + '/E0.csv'
    req = requests.get(csv_url)
    if req.status_code == 200:
        url_content = req.content
        output_file_name = 'PL' + a + '.csv'
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
