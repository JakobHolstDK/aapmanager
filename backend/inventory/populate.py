# command ; serverinfo.py  |jq '.[] | select(."Asset Status" != "Disposed") list all servers that are not disposed
# curl curl http://aapmanager.dsv.com:9990/application/api/applications/ | jq '.[] | select (.Application_Lifecycle_Stage != "Retired" )'
import pprint
import requests
import subprocess
import json
import time
import os
import redis

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", 6379)
redis_db = os.getenv("REDIS_DB", 0)
redis_password = os.getenv("REDIS_PASSWORD", None)
redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_password)
redis_prefix = "inventory"

def create_single_application(data):
    url = "http://aapmanager.dsv.com:9990/inventory/api/appids/"
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return response



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

def get_contries():
    url = "http://aapmanager.dsv.com:9990/inventory/api/countries/"
    response = requests.get(url)
    data = response.json()
    countries = {}
    for country in data:
        countries[country['name']] = country['id']
    return countries


def get_projects():
    url = "http://aapmanager.dsv.com:9990/inventory/api/projects/"
    response = requests.get(url)
    data = response.json()
    projects = {}
    for project in data:
        projects[project['name']] = project['id']
    return projects

def get_Appids():
    url = "http://aapmanager.dsv.com:9990/inventory/api/appids/"
    response = requests.get(url)
    data = response.json()
    appids = {}
    for appid in data:
        appids[appid['appid']] = appid['id']
    return appids

def get_environments():
    url = "http://aapmanager.dsv.com:9990/inventory/api/environments/"
    response = requests.get(url)
    data = response.json()
    environments = {}
    for environment in data:
        environments[environment['name']] = environment['id']
    return environments

def get_regions():
    url = "http://aapmanager.dsv.com:9990/inventory/api/regions/"
    response = requests.get(url)
    data = response.json()
    regions = {}
    for region in data:
        regions[region['name']] = region['id']
    return regions

def get_zones():
    url = "http://aapmanager.dsv.com:9990/inventory/api/zones/"
    response = requests.get(url)
    data = response.json()
    zones = {}
    for zone in data:
        zones[zone['name']] = zone['id']
    return zones

def get_serverroles():
    url = "http://aapmanager.dsv.com:9990/inventory/api/serverroles/"
    response = requests.get(url)
    data = response.json()
    serverroles = {}
    for serverrole in data:
        serverroles[serverrole['name']] = serverrole['id']
    return serverroles

def get_serverinfo():
    url = "http://aapmanager:9990/serverinfo/api/assets/"
    response = requests.get(url)
    data = response.json()
    active_servers = {}
    disposed_servers = {}
    for server in data:
        if server['asset_status'] != "Disposed":
            active_servers[server['host_name']] = server
        else:
            disposed_servers[server['host_name']] = server
    return active_servers, disposed_servers


    
def update_servers():
    data = subprocess.run(["serverinfo.py"], stdout=subprocess.PIPE)

    data = json.loads(data.stdout)
    url = "http://aapmanager.dsv.com:9990/inventory/api/servers/"
    for server in data:
        print(server)
        print("------------------------------")
        payload = { 
            {
                "name": "test",
                "description": "",
                "configitems": null,
                "appid": null,
                "environment": null,
                "region": null,
                "zone": null,
                "serverrole": []
            }
}
            




def main():
    projects = get_projects()
    appids = get_Appids()
    environments = get_environments()
    regions = get_regions()
    zones = get_zones()
    serverroles = get_serverroles()
    countries = get_contries()


    active_servers, disposed_servers = get_serverinfo()

    r = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_password)



    print("we have projects: ", len(projects))
    print("we have appids: ", len(appids))
    print("we have environments: ", len(environments))
    print("we have regions: ", len(regions))
    print("we have zones: ", len(zones))
    print("we have serverroles: ", len(serverroles))
    print("we have countries: ", len(countries))


    print("we have active servers: ", len(active_servers))
    print("we have disposed servers: ", len(disposed_servers ))

    for active_server in active_servers:
        if active_servers[active_server]['application_id'] != "6661":
            continue
        """
        {
          'host_name': 'I16518.DSV.COM',
          'computer_name': 'I16518', 
          'environment': 'Development', 
          'data_center_location': None, 
          'vmware_datacenter': 'DKTAADC03-02', 
          'function': 'CW Template Tool INT', 
          'technical_contacts': 'Jos.Janssen', 
          'country': 'Denmark', 
          'support_hours': '8-17', 
          'guard': 'IT-SOL Support', 
          'application_id': '3327', 
          'application_name': 'CargoWrite WMS Template Tool', 
          'a_number': '', 
          'deploy_date': None, 'asset_status': 'Deployed'}
        """

        get = r.get(f"{redis_prefix}:{active_server}")
        if get == None:
            myappid = "APP-%s" % active_servers[active_server]['application_id']
            appoidid = None
            try:
                appidid = appids[myappid]
            except KeyError:
                appidid = None
            if appidid == None:
                print("Application not found in redis")
                print("------------------------------")
                data = {
                    "appid": myappid,
                    "appname": "unknown",
                    "appowner": "Unknown",
                    "appcontact": "Unknown",
                    "aapstatus": "Active",
                    "configitems": {}
                }
                create_single_application(data)
                appids = get_Appids()
            
            # We now know the appid
            pprint.pprint(active_servers[active_server])
            lowerhost = active_servers[active_server]['host_name'].lower()
            command = ["ansible-inventory",  "-i", "/opt/common/common.inventory",  "--host", lowerhost ]

            data = subprocess.run(command, stdout=subprocess.PIPE)
            data = json.loads(data.stdout)
            print(data)
            for region in regions:
                if region in data['regions']:
                    myregion = regions[region]
                    break
            print("------------------------------")



            myregion = regions['unknown']
            mycontry = "unknown"
            try:
                if active_servers[active_server]['environment'] is not None:
                    lowenvironment = active_servers[active_server]['environment'].lower()
                    myenvironment = environments[lowenvironment]
                else:
                    myenvironment = environments['unknown']
            except KeyError:
                myenvironment = environments['unknown']


            configitems = {
                "host_name": active_servers[active_server]['host_name'],
                "computer_name": active_servers[active_server]['computer_name'],
                "data_center_location": active_servers[active_server]['data_center_location'],
                "vmware_datacenter": active_servers[active_server]['vmware_datacenter'],
                "function": active_servers[active_server]['function'],
                "technical_contacts": active_servers[active_server]['technical_contacts'],
                "country": mycontry,
                "support_hours": active_servers[active_server]['support_hours'],
                "guard": active_servers[active_server]['guard'],
                "application_id": active_servers[active_server]['application_id'],
                "application_name": active_servers[active_server]['application_name'],
                "a_number": active_servers[active_server]['a_number'],
                "deploy_date": active_servers[active_server]['deploy_date'],
                "asset_status": active_servers[active_server]['asset_status']
            }
            try:
                myzone = active_servers[active_server]['zone']
                myzone = zones[myzone]
            except KeyError:
                myzone = zones['unknown']


            myserverdata = {
                "name": active_server,
                "description": "Auotmatically created",
                "configitems": {},
                "appid": appidid,
                "environment": myenvironment,
                "region": myregion,
                "zone": myzone,
                "configitems": configitems

            }
            response = requests.post("http://aapmanager.dsv.com:9990/inventory/api/servers/", json=myserverdata)
            print(response.status_code)
            print(response.text)
            print("------------------------------")
            #r.set(f"{redis_prefix}:{active_server}", json.dumps(active_servers[active_server]), ex=36000)





        else:
            print("Server found in redis")
            print("------------------------------")







    
    #update_applications()
    #update_servers()
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
