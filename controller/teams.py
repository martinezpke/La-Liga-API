from flask import jsonify
from time import sleep
from tqdm.auto import tqdm
from model.information_teams import Teams_information

list_name_teams = ['athletic-club', 'atletico-de-madrid', 'c-a-osasuna', 'cadiz-cf',
                    'elche-c-f', 'fc-barcelona', 'getafe-cf', 'girona-fc',
                    'rayo-vallecano', 'rc-celta', 'rcd-espanyol', 'rcd-mallorca',
                    'real-betis', 'real-madrid', 'real-sociedad', 'r-valladolid-cf',
                    'sevilla-fc', 'ud-almeria', 'valencia-cf', 'villarreal-cf']


def teams_upcoming_matches():
    list_result = list()

    for i in list_name_teams:
        teams = Teams_information(i)
        data_page = teams.teams_information()
        
        data_names = teams.extract_data(
            data_page, 'p', 'styled__TextRegularStyled-sc-1raci4c-0 hvREvZ')
        data_teams_names = teams.extract_data(
            data_page, 'span', 'styled__BreadCrumbItem-zvm62g-1 dcSpNo')
        data_date = teams.extract_data(
            data_page, 'p', 'styled__TextRegularStyled-sc-1raci4c-0 fYuQIM')

        (data, data_name) = json_match(data_teams_names, data_names, data_date)

        list_result.append({'match': data, 'team': data_name})
    return jsonify({"records": list_result})


def teams_games_played():
    list_result = list()

    for i in list_name_teams:
        teams = Teams_information(i)
        data_page = teams.games_played()
        
        data_names = teams.extract_data(
            data_page, 'p', 'styled__TextRegularStyled-sc-1raci4c-0 hvREvZ')
        data_teams_names = teams.extract_data(
            data_page, 'span', 'styled__BreadCrumbItem-zvm62g-1 dcSpNo')
        data_date = teams.extract_data(
            data_page, 'p', 'styled__TextRegularStyled-sc-1raci4c-0 fYuQIM')
        
        (data, data_name) = json_match(data_teams_names, data_names, data_date)
        
        list_result.append({'match': data, 'team': data_name})
    return jsonify({"records": list_result})


def json_match(name, *args):
    list_teams = list()
    list_names = ''
    n = 0
    print("\n")
    print(name[3], "\n")
    for i in tqdm(range(0, len(args[0]), 2)):
        sleep(0.1)
        list_teams.append(
            {'team_home': args[0][i], 'team_away': args[0][i+1],
            'date': args[1][i+n], 'goal_home': args[1][i+n+2], 'goal_away': args[1][i+n+3]})
        n += 2
    list_names = name[3]
    return list_teams, list_names
