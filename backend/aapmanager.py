import requests
import json
import pprint
import libvirt
import xml.etree.ElementTree as ET
import time
import ansible_runner
import base64




class AAPManager:

    def __init__(self):
        self.aapcred = self.load_credentials("data/aapcred.json")
        self.cmdb = self.load_credentials("data/cmdb.json")
        self.aapdata = self.load_credentials("data/aap.json")

        id_secret_bytes = bytes(self.aapcred['username'] + ':' + self.aapcred['password'], 'UTF-8')
        basictoken = base64.b64encode(id_secret_bytes)
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {basictoken}"
        }
       

        self.organizations = self.aap_api("organizations")
        self.organization = self.create_organization()
        self.organizations = self.aap_api("organizations")
        #self.project = self.create_project()
        #self.projects = self.aap_api("projects")

    def create_organization(self):
        url = self.aapcred["url"] + "/api/v2/organizations/"
        data = {
            "name": self.aapdata['organization']['name'],
            "description": self.aapdata['organization']['description']
        }
        response = requests.post(url, headers=self.headers, json=data,  verify=True)
        pprint.pprint(response.text)
        """
        organizations = self.aap_api("organizations")
        pprint.pprint(organizations)
        print("------------------------------------------------")
        url = self.aapcred["url"] + "/api/v2/organizations/" + str(organizations[self.aapdata['organization']]['id']) + "/"
        data = {
            "name": self.aapdata['organization'],
            "description": "5 Autocreated organization",
            }
        response = requests.put(url, headers=headers, json=data,  verify=True)
        """
        return response.status_code
    
    def create_project(self):
        url = self.aapcred["url"] + "/api/v2/projects/"
        organizationid = self.organizations[self.aapdata['organization']]['id']
        data = {
            "name": self.aapdata['mainproject']['name'],
            "organization": organizationid,
            "description": self.aapdata['mainproject']['description']
        }
        id_secret_bytes = bytes(self.aapcred['username'] + ':' + self.aapcred['password'], 'UTF-8')
        basictoken = base64.b64encode(id_secret_bytes)
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {basictoken}"
        }
        response = requests.post(url, headers=headers, json=data,  verify=True)
        projects = self.aap_api("projects")
        url = self.aapcred["url"] + "/api/v2/projects/" + str(projects[self.aapdata['mainproject']]['id']) + "/"
        data = {
            "name": self.aapdata['mainproject']['name'],
            "description": self.aapdata['mainproject']['description']
            }
        response = requests.put(url, headers=headers, json=data,  verify=True)

        return response.status_code

    def load_credentials(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"Error: The file {file_path} does not exist.")
        except json.JSONDecodeError:
            print(f"Error: Failed to parse {file_path}. Ensure it is valid JSON.")
        return None
    
    def aap_api(self, apicall):
        url = self.aapcred["url"] + "/api/login"
        response = requests.post(url, headers=self.headers, verify=True)
        pprint.pprint(response.status_code)
        pprint.pprint(response.text)
        print("------------------------------------------------")

        loop = True
        data = {}
        while loop:
            url = self.aapcred["url"] + "/api/v2/" + apicall
            pprint.pprint(url)
            response = requests.get(url, headers=self.headers, json=data,  verify=True)
            print(response.text)
            try:
                partialdata = json.loads(response.text)
                pprint.pprint(partialdata)
            except json.JSONDecodeError:
                partialdata['count'] = 0 
            if partialdata['count'] == 0:
                loop = False
            if partialdata['next'] == None:
                loop = False
            for mydata in partialdata['results']:
                data[mydata['name']] = mydata
            url = partialdata['next']
        return data
"""
def create_server(data):
    url = "http://127.0.0.1:9999/serverinfo/api/appids/"
    appiddata = {
        "appid": data["appid"],
        "appname": "unknown",
        "appowner": "unknown",
        "appcontact": "unknown"
    }
    response = requests.post(url, json=appiddata)

    url = "http://127.0.0.1:9999/serverinfo/api/servers/"
    response = requests.post(url, json=data)

def load_credentials(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse {file_path}. Ensure it is valid JSON.")
    return None, None


def libvirtinfo():
    
    conn = libvirt.open("qemu:///system")
    domain = conn.lookupByName("awxrpm01")
    domain_config = ET.fromstring(domain.XMLDesc())

    for id in conn.listDomainsID():
        dom = conn.lookupByID(id)
        domain_config = ET.fromstring(dom.XMLDesc())
        data = {
            "hostname": dom.name(),
            "cname": "unknown",
            "description": "unknown",
            "appid": "9999",
            "environment": "unknown",
            "os": "unknown",
            "os_version": "unknown",
            "os_arch": "unknown"
        }
        create_server(data)
        #pprint.pprint(domain_config)
        #print(dom.name())
        #infos = libvirt.virDomainGetInfo(dom)
        #print(infos)
    conn.close()

def serverinfo():
    # Red the data from the file
    # d
    filename = "data/serverinfo.json"
    with open(filename, 'r') as file:
        data = json.load(file)
        for server in data:
            try:
                if server["Asset Status"] == "Disposed":
                    continue
            except KeyError:
                pass
            data = {
                "hostname": server["Host Name"],
                "cname": server["Computer Name"],
                "description": server["Function"],
                "appid": server["Application ID"],
                "environment": server["Environment"],
                "os": "unknown",
                "os_version": "unknown",
                "os_arch": "unknown"
            }
            create_server(data)

            #pprint.pprint(server)

            # Create the server

def aap_create_project(name, organization):
    aapcred = load_credentials("../data/aapcred.json")
    project = {
        "name": name,
        "description": "Autocreated project"
    }
    aapcred = load_credentials("../data/aapcred.json")
    url = aapcred["url"] + "/api/v2/projects/"
    print(url)
    print("-----------------")
    headers = { 
        "Content-Type": "application",
        "Authorization": f"Bearer {aapcred['token']}"
    }
    response = requests.post(url, headers=headers, json=data,  verify=True)
    pprint.pprint(response.status_code)

    return response.status_code



def aap_api(apicall):
    aapcred = load_credentials("../data/aapcred.json")
    loop = True
    data = {}
    while loop:
        url = aapcred["url"] + "/api/v2/" + apicall
        headers = { 
            "Content-Type": "application",
            "Authorization": f"Bearer {aapcred['token']}"
        }
        response = requests.get(url, headers=headers, json=data,  verify=True)
        try:
            partialdata = json.loads(response.text)
        except json.JSONDecodeError:
            partialdata = None
        if partialdata['count'] == 0:
            loop = False
        if partialdata['next'] == None:
            loop = False
        for mydata in partialdata['results']:
            data[mydata['name']] = mydata
        url = partialdata['next']

    return data


def aap_cmdb():
    cmdb = load_credentials("../data/cmdb.json")
    if not cmdb:
        return
    try:
        if cmdb['libvirt']:
            libvirtinfo()
    except KeyError:
        pass
    try:
        if cmdb['serverinfo']:
            serverinfo()
    except KeyError:
        pass
"""
def main():
    aapenv = AAPManager()

    return

    aapdata = load_credentials("../data/aap.json")
    try: 
        orginisation = aapdata['organization']
    except KeyError:
        print("Error: Organization not defined")
        return
    try:
        projects = aapdata['mainproject']
    except KeyError:
        print("Error: Mainproject not defined")
        return
    
    orginisations = aap_api("organizations")
    projects = aap_api("projects")


    aap_create_project(aapdata['mainproject'], orgid)



        
    
    
    aaplicatioons = aap_api(f"organizations/{orgid}/applications")
    #pprint.pprint(orginisations)



    

if __name__ == "__main__":
    main()


#data = {
#    "hostname": "testserver",
#    "cname": "testserver.example.com",
#    "description": "a test server",
#½    "appid": "6661",
#    "environment": "PROD",
#    "os": "RHEL",
#    "os_version": "8.4",
#    "os_arch": "x86_64",
#}


#{'A-Number': '',
# 'Application ID': '2280',
# 'Application Name': 'Citrix Global Desktop',
# 'Asset Status': 'Disposed',
# 'Computer Name': 'I12039',
# 'Country': 'DSV Group',
# 'DataCenterLocation': 'DKCPHDC01',
# 'DeployDate': '03/30/2018 10:46',
# 'Environment': 'Production',
# 'Function': 'Citrix XenApp Server',
# 'Guard': None,
# 'Host Name': 'I12039.DSV.COM',
# 'Support Hours': '8-17',
# 'Technical Contacts': 'jan.toftvang;rommel.niechun',
# 'VMWare Datacenter': None}
