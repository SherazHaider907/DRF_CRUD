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
    
# post_data()

# update method
# partial update mean single value of data
def update_data():
    data = {
        'id':4,
        'name':'haiderAli',
        'roll':4,
        'city':'kotmomin'
    }
    json_data = json.dumps(data)
    resp = requests.put(url=URL, data=json_data)
    data = resp.json()
    print(data)
update_data()