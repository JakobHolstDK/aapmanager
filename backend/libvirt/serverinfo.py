import libvirt
import xml.etree.ElementTree as ET
import pprint


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
  print(id)
  dom = conn.lookupByID(id)
  print(dom.name())


#    infos = libvirt.virDomainGetInfo(dom)

