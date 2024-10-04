import libvirt
import xml.etree.ElementTree as ET
import pprint
import json
import requests


def load_credentials(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            username = data.get('username')
            password = data.get('password')
            return username, password
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse {file_path}. Ensure it is valid JSON.")
    return None, None




conn = libvirt.open("qemu:///system")
domain = conn.lookupByName("awxrpm01")
domain_config = ET.fromstring(domain.XMLDesc())

for id in conn.listDomainsID():
    print("------------------------")
    dom = conn.lookupByID(id)
    print(dom.name())
    data = {
    "name": dom.name(),
    "description": "This is a libvirt server",
    "configitems": "",
    "appid": 3,
    "environment": 6,
    "region": 5,
    "zone": 3,
    "serverrole": [4,5]
    }

    headers = {
    'Content-Type': 'application/json',
    }
    print(json.dumps(data))
    url = 'http://127.0.0.1:9990/inventory/apiservers/'
    response = requests.post(url, headers=headers, data=json.dumps(data))   
    print(response.status_code)
    print(response.text)







#    infos = libvirt.virDomainGetInfo(dom)

