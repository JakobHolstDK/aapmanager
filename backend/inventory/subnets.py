import redis
import json 
import os
import sys
import time
import subprocess
import pydig
import socket
import pprint
import requests





def main():
    r = redis.Redis(host='localhost', port=6379, db=0)
    subnets = {}
    dmzserver = {}
    zone = {}

    keys = r.keys("serverinfo:netcat:*")
    for key in keys:
        server = key.decode("utf-8").split(":")[2]
        value = r.get(key).decode("utf-8")
        if value == "0":
            dig = pydig.query(server, 'A')
            for ip in dig:
                try:
                    socket.inet_aton(ip)
                    # replace last octet with 0
                    ip = ip.rsplit(".", 1)[0] + ".0"
                    splitmyserver = server.lower().split(".")
                    subnets[ip] = splitmyserver[1]
                    try:
                        myzone = zone[splitmyserver[1]] 
                    except KeyError:
                        zone[splitmyserver[1]] = []

                    zone[splitmyserver[1]].append(ip)
                                                   

                except socket.error:
                    pass

    

result = requests.get("http://aapmanager:9990/serverinfo/api/assets/")
try:
  assets = result.json()
except json.decoder.JSONDecodeError:
  print("Error: Unable to decode JSON")
  sys.exit(1)

for asset in assets:
    print(asset)
    




    

if __name__ == '__main__':
    main()
