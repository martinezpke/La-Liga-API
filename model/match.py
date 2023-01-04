import requests
from model.data_table import Data_table
from bs4 import BeautifulSoup


class Match(Data_table):

    def __init__(self, number_of_journeys, number, *args) -> None:
        self.number_of_journeys = number_of_journeys
        self.name_class_1 = args[0]
        self.name_class_2 = args[1]
        self.number = number


    def journeys(self):
        try:
            url = 'https://www.laliga.com/laliga-santander/resultados/2022-23/jornada-{0}'.format(self.number)

            requests_match = requests.request('GET', url, headers={'User-Agent': "Mozilla/5. \
                (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/91.0.4472.124 Safari/537.36 edg/91.0.864.59 "})

            soup = BeautifulSoup(requests_match.content, 'html.parser')

            soup_match = soup.find_all('p', class_=self.name_class_1)
            result = super().add_information(soup_match)
            
            soup_match_date = soup.find_all('p', class_=self.name_class_2)
            result_date = super().add_information(soup_match_date)

            match_result = self.add_match(result, result_date)
            
            return match_result
        except ValueError as e:
            print(e.message)


    def add_match(self, *args):
        try:
            n = 0; h = 0;
            list_teams = list()
            
            for i in range(10):
                list_teams.append(
                    {'team_home': args[0][n], 'team_away': args[0][n+1], 'date': args[1][h], 'hours': args[1][1+h],
                        'goal_Home': args[1][2+h], 'goal_away': args[1][3+h]})
                n += 2
                h += 4
            return list_teams
        except Exception as e:
            print(e)
            n = 0; h = 0;
            list_teams = list()
            
            for i in range(10):
                list_teams.append(
                    {'team_home': args[0][n], 'team_away': args[0][n+1], 'date': args[1][h], 'hours': args[1][h+1]})
                n += 2
                h += 2
            return list_teams
            