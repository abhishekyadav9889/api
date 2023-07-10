import requests
import json


URL= " http://127.0.0.1:8001/sutcreate/"
data={
    'fast_name':'sonam',
    'last_Name':'yadav',
    'roll_No': 101,
    'ctye':'Rachi'
}
json_data= json.dumps(data)
r = requests.post(url=URL,data=data)

data=r.json()
print(data) 