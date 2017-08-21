import json
import sys
import shutil
from pprint import pprint
from git import Repo
import tarfile
import os

SRC_PATH="/home/sravanthi/Videos/automation-labs/"
DEST_PATH="/home/sravanthi/Videos/automation-labs-tar/"
   
with open('labs.json') as data_file:    
    data = json.load(data_file)
    for i in range(91):
        repo_name = (data[i]["name"].encode("utf-8"))
        repo_url = (data[i]["html_url"].encode("utf-8"))
        os.chdir(SRC_PATH)
        if not os.path.isdir(repo_name):
            Repo.clone_from(repo_url, repo_name)

        tar_cmd = ("tar -cvf %s.tar.gz %s" % (DEST_PATH+repo_name, repo_name))

        os.system(tar_cmd)

    #print os.system("ls")
     # #    print( repo_name + ".tar.gz" ) 
#     with tarfile.open(repo_name + ".tar.gz", "w:gz" ) as tar:
#         for name in os.chdir("/home/sravanthi/Videos/automation-labs-tar"):
#             tar.add(name)
