#!/bin/bash
# The script clones all repositories of an GitHub organization.

# the github organization to fetch all repositories for

#GITHUB_ORGANIZATION=vlabs-on-openedx

# the git clone cmd used for cloning each repository
# the parameter recursive is used to clone submodules, too.

#GIT_CLONE_CMD="git clone https://github.com/vlabs-on-openedx/*.git"

# fetch repository list via github api
# grep fetches the json object key ssh_url, which contains the ssh url for the repository

#REPOLIST=`curl --silent https://api.github.com/orgs/${GITHUB_ORGANIZATION}/repos?per_page=200 -q | grep "\"ssh_url\"" | awk -F': "' '{print $2}' | sed -e 's/",//g'`

# loop over all repository urls and execute clone

#for REPO in $REPOLIST; do
 # ${GIT_CLONE_CMD}${REPO}
#done

import requests
import json
import subprocess

GITHUB_ORGANIZATION = "vlabs-on-openedx"
ACCESS_TOKEN="99a193a069e034c5f87f75d8cc7cfe217ab51a1c"
CLONE_DIR="/home/sravanthi/Music/automation-labs"

r = requests.get("https://api.github.com/orgs/" + vlabs-on-openedx + "/repos?per_page=100&access_token=" + ACCESS_TOKEN )

data = json.loads(r.text)

for repo in data:
    print repo['full_name']
    p = subprocess.Popen(["git","clone", repo['https://github.com/vlabs-on-openedx']], cwd=CLONE_DIR)  
    p.wait()
