import requests

endpoint = 'https://cell-content-type.azurewebsites.net/api/content_type.json'

def query(content):
    params = {'content':content}
    response = requests.get(endpoint, params=params)
    #print(response.status_code)
    #print(response.headers)
    return response.json()