import json
import sys
import shutil
from pprint import pprint
from git import Repo
import tarfile
import os

   
with open('labs.json') as data_file:    
    data = json.load(data_file)
    for i in range(2):
        repo_name = (data[i]["name"].encode("utf-8"))
        repo = (data[i]["html_url"].encode("utf-8"))
        
       # print("/home/sravanthi/Videos/automation-labs/" + repo_name)
        Repo.clone_from(repo, "/home/sravanthi/Videos/automation-labs/" + repo_name)

 #       shutil.make_archive(i.zip, 'zip', vlabs-automation-labs)

 
#folder_path = ("/home/sravanthi/Videos/automation-labs/" + repo_name) 
with tarfile.open(  (data[i]["name"].encode("utf-8")) + ".tar.gz", "w:gz" ) as tar:
    for name in os.listdir("/home/sravanthi/Videos/automation-labs/")
    for name in shutil.move( "/home/sravanthi/Videos/build-vlabs-on-openedx/*", "/home/sravanthi/Videos/automation-labs-tar/" ):
        tar.add(name)
