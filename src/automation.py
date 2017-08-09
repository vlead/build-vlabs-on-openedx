import json
from pprint import pprint

with open('gitrepos.json') as data_file:    
    data = json.load(data_file)
    for i in range(100):
        pprint (data[i]["html_url"].encode("utf-8"))
