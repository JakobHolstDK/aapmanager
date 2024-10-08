

import requests
import subprocess
import json
import time
import redis
import os

import pydig

def dnsdig(hostname):
    dig = pydig.query(hostname, "A")
    return dig


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
    redis_host = os.getenv("REDIS_HOST", "localhost")
    redis_port = os.getenv("REDIS_PORT", 6379)
    redis_db = os.getenv("REDIS_DB", 0)
    redis_password = os.getenv("REDIS_PASSWORD", None)
    redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_password)
    redis_prefix = "serverinfo"



  # get the serverinfo.py data with subprocess
    data = subprocess.run(["serverinfo.py"], stdout=subprocess.PIPE)
    # convert the data to json
    data = json.loads(data.stdout)
    
    # for each server in the data
    for server in data:
        try:
            serverupdate = redis_client.get(f"{redis_prefix}:{server['Host Name']}")
            print(serverupdate)


        except Exception as e:
            print(e)
            serverupdate = None

        if serverupdate == None:
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
            if response.status_code == 201 or response.status_code == 400:
                pass 
            else:
                print("Error sending data")
                print(response.text)
                print(response.status_code)

            time.sleep(0.02)
            redis_client.set(f"{redis_prefix}:{server['Host Name']}", json.dumps(digested_server), ex=3600)
        else:
            print(f"Server {server['Host Name']} already in the database")
            print(serverupdate)
            print("------------------------------")
        rediskey = redis_prefix + ":dig:" + server["Host Name"]
        diginfo = redis_client.get(rediskey)
        if diginfo == None:
            print(f"Server {server['Host Name']} not in the dig database")
            print("--------------Dig------------------")
            mydig = dnsdig(server["Host Name"])
            print(mydig)
            redis_client.set(rediskey, mydig, ex=3600)

        else:
            print(f"Server {server['Host Name']} already in the dig database")
            print(diginfo)
            print("--------------Dig------------------")

        

    # g 
        resdiskey = redis_prefix + ":netcat:" + server["Host Name"]
        netcatinfo = redis_client.get(resdiskey)
        if netcatinfo == None:
            print(f"Server {server['Host Name']} not in the netcat database")
            print("-------------Netcat-----------------")
            netcat = os.system(f"nc -zv {server['Host Name']} 22")
            print(netcat)
            redis_client.set(resdiskey, netcat, ex=3600)
            
        else:
            print(f"Server {server['Host Name']} already in the netcat database")
            print(netcatinfo)
            print("--------------netcat----------------")
    return

if __name__ == "__main__":
    main()



