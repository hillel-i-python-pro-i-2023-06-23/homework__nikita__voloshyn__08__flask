import requests


def get_number_of_astronauts():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    data = response.json()
    number_of_astronauts = data["number"]
    astronauts = [astronaut["name"] for astronaut in data["people"]]
    return number_of_astronauts, astronauts
