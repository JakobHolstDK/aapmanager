#!/usr/bin/env bash




awx-cli organization create --name "AAPDEMO" --description "Ansible Automation demo" >/dev/null 2>&1
ORGID=$(awx-cli organization list | jq '.results[] | select(.name == "AAPDEMO") | .id')
SCMCREDTYPE=$(awx-cli credential_type list | jq '.results[] | select(.name == "Source Control") | .id')
awx-cli team create --name "AAPDEMO" --organization $ORGID >/dev/null 2>&1
awx-cli user create --username "AAPDEMO" --password "ixj90j2s" --email "demo@openknowit.com" >/dev/null 2>&1
awx-cli team associate --team "AAPDEMO" --user "AAPDEMO" >/dev/null 2>&1
USERID=$(awx-cli user list | jq '.results[] | select(.username == "AAPDEMO") | .id')
TEAMID=$(awx-cli team list | jq '.results[] | select(.name == "AAPDEMO") | .id')
project

sshkey=$(cat data/aapdemo | tr -d '\n')
inputjson=$(python readkey.py) 
echo $inputjson |jq . > data/scmcred.json
awx-cli credential create --name cred_AAPDEMO-bitbucket  --description "Ansible automation scm credential" --organization $ORGID  --credential-type $SCMCREDTYPE  --inputs  @$PWD/data/scmcred.json 
GITCRED=$(awx-cli credential list | jq '.results[] | select(.name == "cred_AAPDEMO-bitbucket") | .id')

awx-cli project create --monitor --wait --name \"AAPDEMO\" --description \"Ansible Automation Demo\"  --scmtype "git" --scmurl "git@bitbucket.org:team-nine/aapdemo.git"  --scm_branch "main" --scm_clean 1 --scm_delete_on_update 1  --credential $GITCRED --organization $ORGID  --scm_update_on_launch 1  







