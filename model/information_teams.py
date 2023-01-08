import requests
from model.data_table import Data_table
from bs4 import BeautifulSoup


class Teams_information(Data_table):
    
    def __init__(self, name_teams):
        self.name_teams = name_teams
        
    
    def teams_information(self):
        url = 'https://www.laliga.com/clubes/{0}/proximos-partidos'.format(self.name_teams)
        
        # we need to extract the teams information
        page = requests.request('GET', url, headers={'User-Agent': "Mozilla/5. \
            (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/91.0.4472.124 Safari/537.36 edg/91.0.864.59 "})
        
        soup =  BeautifulSoup(page.content, 'html.parser')
        
        return soup
    
    
    def games_played(self):
        url = 'https://www.laliga.com/clubes/{0}/resultados'.format(self.name_teams)
        
        # we need to extract the teams information
        page = requests.request('GET', url, headers={'User-Agent': "Mozilla/5. \
            (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/91.0.4472.124 Safari/537.36 edg/91.0.864.59 "})
        
        soup =  BeautifulSoup(page.content, 'html.parser')
        
        return soup
        
    
    def extract_data(self, soup, elements, class_name):
        data = soup.find_all(elements, class_=class_name)
        result = super().add_information(data)
        return result