import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"
# read operation
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    resp = requests.get(url=URL, data=json_data)
    data = resp.json()
    print(data)
# get_data()

# create method post method
def post_data():
    data = {
        'name':'sheraz',
        'roll':123,
        'city':'kot'
    }
    json_data = json.dumps(data)
    resp = requests.post(url=URL, data=json_data)
    data = resp.json()
    print(data)
    
post_data()
