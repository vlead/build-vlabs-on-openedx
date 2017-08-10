
import json
from pprint import pprint
from git import Repo
import sys
   
with open('labs.json') as data_file:    
    data = json.load(data_file)
    for i in range(5):
        repo_name = (data[i]["name"].encode("utf-8"))
        repo = (data[i]["html_url"].encode("utf-8"))
        
#        print("/home/sravanthi/Music/automation-labs/" + repo_name)
        Repo.clone_from(repo, "/home/sravanthi/Music/automation-labs/" + repo_name)
