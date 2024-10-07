

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
    digesteddata =     {
    "host_name": data["Host Name"],
    "computer_name": data["Computer Name"],
    "environment": data["Environment"],
    "data_center_location": data["DataCenterLocation"],
    "vmware_datacenter": data["VMWare Datacenter"],
    "function": data["Function"],
    "technical_contacts": data["Technical Contacts"],
    "country": data["Country"],
    "support_hours": data["Support Hours"],
    "guard": data["Guard"],
    "application_id": data["Application ID"],
    "application_name": data["Application Name"],
    "a_number": data["A-Number"],
    "deploy_date": data["DeployDate"],
    "asset_status": data["Asset Status"]
    }
    # for each server in the data
    for server in digesteddata:
        print(server)

        # post the data to the server
        response = requests.post("http://aapmanager.dsv.com:9990/serverinfo/api/assets/", data=server, verify=False)
        print(response.text)
        time.sleep(1)
    return

if __name__ == "__main__":
    main()



