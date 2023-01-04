import requests
from bs4 import BeautifulSoup


class Data_table:

    def __init__(self, *args) -> None:
        self.table = []
        self.class_data = args[0]

    def data(self, url):
        # this take the HTML of the url
        page = requests.request("GET", url, headers={'User-Agent': "Mozilla/5. \
            (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/91.0.4472.124 Safari/537.36 edg/91.0.864.59 "})

        # this do the convert to Beautiful format. it allow identify the different element from HTML
        soup = BeautifulSoup(page.content, 'html.parser')

        data_result = soup.find_all(
            'p', class_='styled__TextRegularStyled-sc-1raci4c-0 cIcTog')
        result = self.add_information(data_result)

        name = soup.find_all(
            'p', class_='styled__TextRegularStyled-sc-1raci4c-0 glrfl')
        name_result = self.add_information(name)

        # add information to table
        tabla = self.add_table(result, name_result)

        return tabla

    # this need a parameter fot it can add information to list

    def add_information(self, data):
        list_teams = list()
        for teams_x in data:
            if teams_x.text != list_teams:
                list_teams.append(teams_x.text)
        return list_teams

    # this need two parameters for it can add information to table of teams and resulted

    def add_table(self, *args):
        p = 0
        n = 0
        list_teams = list()

        for i in range(20):
            list_teams.append(
                {'name': args[1][n+1], 'name2': args[1][n], 'PTS': args[0][10+p], 'PJ': args[0][11+p], 'PG': args[0][12+p], 'PE': args[0][13+p],
                    'PP': args[0][14+p], 'GF': args[0][15+p], 'GC': args[0][16+p], 'DG': args[0][17+p]})
            p += 8
            n += 2

        return list_teams
