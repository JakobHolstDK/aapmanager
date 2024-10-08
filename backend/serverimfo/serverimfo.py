
import pprint
import requests
import subprocess
import json
import time
import redis
import os

import pydig

def dnsdig(hostname):
    mydig = subprocess.run(["dig", hostname], stdout=subprocess.PIPE)
    dig = mydig.stdout.decode("utf-8")
    return dig
def answer_section(dns_response):
    if dns_response == None:
        return None
    lines = dns_response.splitlines()
    answer_section = False
    answer = ""
    for line in lines:
        if "ANSWER SECTION" in line:
            answer_section = True
            continue
        if "AUTHORITY SECTION" in line:
            break
        if answer_section and line.strip():
            answer += line + "\n"
    return answer


def is_answer_section_populated(dns_response):
    if dns_response == None:
        return False
    
    # Split the DNS response into lines
    lines = dns_response.splitlines()
    
    # Look for the "ANSWER SECTION" header
    answer_section_found = False
    for line in lines:
        if "ANSWER SECTION" in line:
            answer_section_found = True
            continue  # Go to the next line after "ANSWER SECTION"
        
        # If the answer section is found and the next line has content, return True
        if answer_section_found and line.strip():
            return True

    # Return False if no content is found after the "ANSWER SECTION"
    return False


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
        except Exception as e:
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

            time.sleep(0.02)
            redis_client.set(f"{redis_prefix}:{server['Host Name']}", json.dumps(digested_server), ex=36000)
        else:
            pass
        rediskey = redis_prefix + ":dig:" + server["Host Name"]
        try:
            diginfo = redis_client.get(rediskey).decode("utf-8")
        except Exception as e:
            diginfo = None

        if diginfo == None and server["Host Name"] not in ["local.dev", "localhost"]:

            mydig = dnsdig(server["Host Name"])
            redis_client.set(rediskey, mydig, ex=36000)

        else:
            pass

        
    # g if answer section 
        if answer_section(diginfo) != "" and answer_section(diginfo) != None:
            pprint.pprint(answer_section(diginfo))
            resdiskey = redis_prefix + ":netcat:" + server["Host Name"]
            netcatinfo = redis_client.get(resdiskey)
            if netcatinfo == None:
                netcat = os.system(f"timeout 1 nc -zv {server['Host Name']} 22 2>/dev/null" )
                redis_client.set(resdiskey, netcat, ex=360000)
            else:
                pass
            
        if answer_section(diginfo) != "" and answer_section(diginfo) != None:
            #{"detected":["Date has wrong format. Use one of these formats instead: YYYY-MM-DD."],"updated":["Date has wrong format. Use one of these formats instead: YYYY-MM-DD."],"os":["
            detected = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            myserverdata = {
            "hostname": server["Host Name"],
            "cname": "in progress",
            "description": "in progress",
            "environment": "unknown",
            "detected": detected,
            "updated": detected,
            "status": "unknown",
            "os": "",
            "os_version": "",
            "os_arch": "",
            "os_lastboot": "",
            "os_lastpatch": "",
            "os_uptime": "",
            "os_installed": "",
            "os_lastmodified": "",
            "os_eol_state": "",
            "appid": server["Application ID"],
            }
            
            rediskey = redis_prefix + ":serverdate" + server["Host Name"]
            try:
                serverdata = redis_client.get(rediskey).decode("utf-8")
            except Exception as e:
                serverdata = None
    
            if serverdata == None:
                print("Sending data for serverdata")
                response = requests.post("http://aapmanager.dsv.com:9990/serverinfo/api/servers/", data=myserverdata, verify=False)
                print(response.status_code)
                print(response.text)
                print("------------------------------------------------")
                if response.status_code == 201 or response.status_code == 400:
                    pass
                else:
                    print("Error sending data")
                redis_client.set(rediskey, json.dumps(myserverdata), ex=36000)
            else:
                pass
    
    return

if __name__ == "__main__":
    main()



