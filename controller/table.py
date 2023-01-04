from flask import jsonify
from model.data_table import Data_table


def show():
    # this is the url of the page we want to scrape
    url = 'https://www.laliga.com/laliga-santander/clasificacion'

    # tell the object to get the url
    data = Data_table('styled__ContainerAccordion-e89col-11 HquGF')
    team = data.data(url)

    return jsonify({"records": team})

