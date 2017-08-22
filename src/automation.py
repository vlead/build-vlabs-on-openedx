import json
import sys
import subprocess
import os

os.system('sudo apt-get install python-pip')                
#easy_install pip

import pip

os.environ["HTTP_PROXY"] = "http://proxy.iiit.ac.in:8080"
os.environ["HTTPS_PROXY"] = "http://proxy.iiit.ac.in:8080"

pip.main(['install', 'gitpython'])

from pprint import pprint
from git import Repo
import tarfile


os.system("wget https://api.github.com/orgs/vlabs-on-openedx/repos?per_page=92")
os.rename('repos?per_page=92','edxrepos.json')
   

SRC_PATH= "../edx_repos"
DEST_PATH = "../edx_tarfiles"

os.makedirs('../edx_repos')
os.makedirs('../edx_tarfiles')

with open('edxrepos.json') as data_file:    
    data = json.load(data_file)
    
    for i in range(91):
        repo_name = (data[i]["name"].encode("utf-8"))
        repo_url = (data[i]["html_url"].encode("utf-8"))
        os.chdir(SRC_PATH)


        if not os.path.isdir(repo_name):
            Repo.clone_from(repo_url, repo_name)

        os.chdir(DEST_PATH)   
        tar_cmd = ("tar -cvf %s.tar.gz %s/%s" % (repo_name, SRC_PATH, repo_name))

        os.system(tar_cmd)

