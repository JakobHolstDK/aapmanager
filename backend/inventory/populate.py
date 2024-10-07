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
        if application["Application_has_Technical_Subject_Matter_Expert_Name"] == "":
          application["Application_has_Technical_Subject_Matter_Expert_Name"] = "Unknown"

        if application["Application_has_Service_Owner_Name"] == "":
          application["Application_has_Service_Owner_Name"] = "Unknown"
        payload = {
            "appid": application["Identifier"],
            "appname": application["Name"],
            "appowner": application["Application_has_Service_Owner_Name"],
            "appcontact": application["Application_has_Technical_Subject_Matter_Expert_Name"],
            "aapstatus": "Active",
            "configitems": {}
            }
        
        
        if application["Application_Lifecycle_Stage"] != "Retired":
            application["Application_Lifecycle_Stage"] = "Retired"
            response = requests.post(dest_url, json=payload, verify=False)
            print(response.status_code)
            print(response.text)

            print(f"Updated application {application['Name']}")
            time.sleep(0.1)
        else:
            print(f"Application {application['Name']} is already retired")
            time.sleep(0.1)

    
def update_servers():
    data = subprocess.run(["serverinfo.py"], stdout=subprocess.PIPE)

    data = json.loads(data.stdout)
    url = "http://aapmanager.dsv.com:9990/inventory/api/servers/"
    for server in data:
        print(server)
        print("------------------------------")




def main():
    
    #update_applications()
    update_servers()
    return



    
    

"""



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
"""

if __name__ == "__main__":
    main()
