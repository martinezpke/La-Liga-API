from flask import Flask, jsonify
from controller.table import show
from controller.match_controller import match

server = Flask("La-liga")

@server.get('/index')
def index():
    return jsonify({'messenger': "Welcome Api the (La liga)"})

@server.get('/table')
def table():
    return show()


@server.route('/journeys-<number>', methods=['GET'])
def journeys(number):
    return match(number)


if __name__ == "__main__":
    server.run(debug=True)