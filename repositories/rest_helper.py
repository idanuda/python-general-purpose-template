import requests


def get(url):
    response = requests.get(url)
    return response.text


def post(url, data):
    response = requests.post(url, data)
    return response.text
