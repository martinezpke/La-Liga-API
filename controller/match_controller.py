from model.match import Match
from flask import jsonify, abort

def match(number):
    # we declare the variables name_class y number_of_journeys because the objet need this data
    name_class_1 = 'styled__TextRegularStyled-sc-1raci4c-0 hvREvZ'
    name_class_2 = 'styled__TextRegularStyled-sc-1raci4c-0 fYuQIM'
    number_of_journeys = 38
    
    if int(number) > number_of_journeys:
        return abort(404)
    
    else:
        data_match = Match(number_of_journeys, number, name_class_1, name_class_2)
        
        data = data_match.journeys()
        return jsonify({"records": data}),200