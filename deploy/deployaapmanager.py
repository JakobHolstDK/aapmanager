#!/usr/bin/env python
# 
import subprocess
import sys
import os
import json
import time

# script to run git pull and deploy if brach has changed

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')
def run_cmd_background(cmd):
    subprocess.Popen(cmd, shell=True)
    return


def main():
    while True:
        print("Version 1.1.0.2")
        print("Deploying aapmanager")
        remote_host = "aapmanager"
        remote_dir = "/opt/aapmanager/development/"
        run_cmd("git fetch")
        # get the current branch
        current_branch = run_cmd("git rev-parse --abbrev-ref HEAD").strip()
        # get the remote branch
        remote_branch = run_cmd("git rev-parse --abbrev-ref --symbolic-full-name @{u}").strip()
        # get the remote branch name
        remote_branch_name = remote_branch.split("/")[1]
        # get the remote branch hash
        remote_branch_hash = run_cmd("git rev-parse HEAD").strip()
        # get the remote branch hash
        current_branch_hash = run_cmd("git rev-parse @{u}").strip()
        # check if the remote branch has changed
        if remote_branch_hash != current_branch_hash:
            print(f"Branch {current_branch} has changed, deploying branch {remote_branch_name}")
            # deploy the remote branch
            run_cmd("git checkout " + remote_branch_name)
            run_cmd("git pull")
            run_cmd("scp -r ./* " + remote_host + ":" + remote_dir)
            run_cmd("ssh aapmanager /opt/aapmanager/development/aapmgr/venv/bin/pip install -r /opt/aapmanager/development/aapmgr/requirements.txt")
            run_cmd("ssh aapmanager /opt/aapmanager/development/aapmgr/venv/bin/python /opt/aapmanager/development/aapmgr/manage.py migrate")
            run_cmd("ssh aapmanager /opt/aapmanager/development/aapmgr/venv/bin/python /opt/aapmanager/development/aapmgr/manage.py collectstatic --noinput")
            run_cmd("ssh aapmanager systemctl --user restart aapmanager")
        else:
            print(f"Branch {current_branch} has not changed")

        # ensure we have a ssh port forward to the remote host
        run_cmd_background("ssh -L 5432:localhost:5432 aapmanager sleep 60000")
        print("Sleeping for 10 seconds")
        time.sleep(10)
        print("loooooooooop")

    
if __name__ == "__main__":
    main()


                