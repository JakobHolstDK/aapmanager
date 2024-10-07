# command ; serverinfo.py  |jq '.[] | select(."Asset Status" != "Disposed") list all servers that are not disposed
# curl curl http://aapmanager.dsv.com:9990/application/api/applications/ | jq '.[] | select (.Application_Lifecycle_Stage != "Retired" )'

import requests
import subprocess
import json
import time
import os


def update_applications():
    url = "http://aapmanager.dsv.com:9990/application/api/applications/"
    dest_url = "http://aapmanager.dsv.com:9990/inventory/api/appids/"
    response = requests.get(url)
    data = response.json()

    for application in data:
        payload = {
            "appid": data["Identifier"],
            "appname": data["Name"],
            "appowner": data["Application_has_Service_Owner_Name"],
            "appcontact": data["Application_has_Technical_Subject_Matter_Expert_Name"],
            "aapstatus": data["Application_Lifecycle_Stage"],
            "configitems": {}
            }
        
        if application["Application_Lifecycle_Stage"] != "Retired":
            application["Application_Lifecycle_Stage"] = "Retired"
            response = requests.post(dest_url, json=payload, verify=False)
            print(f"Updated application {application['Name']}")

    


def main():
    
    update_applications()
    
    
    





    # get the serverinfo.py data with subprocess
    data = subprocess.run(["serverinfo.py"], stdout=subprocess.PIPE)
    # convert the data to json
    data = json.loads(data.stdout)
    
    # for each server in the data
    for server in data:
        digested_server = {
            "hostname": server["Host Name"],
            "computername": server["Computer Name"],
            "environment": server["Environment"],
            "datacenterlocation": server["DataCenterLocation"],
            "vmwaredatacenter": server["VMWare Datacenter"],
            "function": server["Function"],
            "technicalcontacts": server["Technical Contacts"],
            "country": server["Country"],
            "supporthours": server["Support Hours"],
            "guard": server["Guard"],
            "applicationid": server["Application ID"],
            "applicationname": server["Application Name"],
            "anumber": server["A-Number"],
            "deploydate": server["DeployDate"],
            "assetstatus": server["Asset Status"]
        }
        # post the server to the serverinfo api
        requests.post("http:///", json=digested_server)
        print(f"Posted server {server['Host Name']}")