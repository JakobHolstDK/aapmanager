

import requests
import subprocess
import json
import time
import os

# the command serverinfo.py generates the following output:
"""
[
  {
    "Host Name": "demo.example.com",
    "Computer Name": "demo",
    "Environment": null,
    "DataCenterLocation": null,
    "VMWare Datacenter": null,
    "Function": null,
    "Technical Contacts": null,
    "Country": null,
    "Support Hours": "8-17",
    "Guard": null,
    "Application ID": "-blank-",
    "Application Name": null,
    "A-Number": "",
    "DeployDate": null,
    "Asset Status": "Disposed"
  },
    {
        "Host Name": "demo2.example.com",
        "Computer Name": "demo2",
        "Environment": null,
        "DataCenterLocation": null,
        "VMWare Datacenter": null,
        "Function": null,
        "Technical Contacts": null,
        "Country": null,
        "Support Hours": "8-17",
        "Guard": null,
        "Application ID": "-blank-",
        "Application Name": null,
        "A-Number": "",
        "DeployDate": null,
        "Asset Status": "Disposed"
    }
]
"""

# the data must be poste one by one to the server
# we need to get the current data from the api first

def main():
  # get the serverinfo.py data with subprocess
    data = subprocess.run(["serverinfo.py"], stdout=subprocess.PIPE)
    # convert the data to json
    data = json.loads(data.stdout)
    
    # for each server in the data
    for server in data:
        print(server)
        digested_server = {
            "host_name": server["Host Name"],
            "computer_name": server["Computer Name"],
            "environment": server["Environment"],
            "datacenterlocation": server["DataCenterLocation"],
            "vmware_datacenter": server["VMWare Datacenter"],
            "function": server["Function"],
            "technical_contacts": server["Technical Contacts"],
            "country": server["Country"],
            "support_hours": server["Support Hours"],
            "guard": server["Guard"],
            "application_id": server["Application ID"],
            "application_name": server["Application Name"],
            "a_number": server["A-Number"],
            "deploydate": server["DeployDate"],
            "asset_status": server["Asset Status"]
        }


        # post the data to the server
        response = requests.post("http://aapmanager.dsv.com:9990/serverinfo/api/assets/", data=digested_server, verify=False)
        print(response.text)
        time.sleep(0.1)
    return

if __name__ == "__main__":
    main()



