from flask import Flask, jsonify
from controller.table import show
from controller.match_controller import match
from controller.teams import teams_upcoming_matches, teams_games_played

server = Flask("La-liga")

@server.get('/')
def index():
    return jsonify({'messenger': "Welcome Api the (La liga)"})

@server.get('/table')
def table():
    return show()


@server.get('/journeys-<number>')
def journeys(number):
    return match(number)


@server.get('/teams/upcoming-matches')
def upcoming_matches():
    return teams_upcoming_matches()


@server.get('/teams/games-played')
def games_played():
    return teams_games_played()

if __name__ == "__main__":
    server.run(debug=True)