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

    

    for key in zone:
        for ip in zone[key]:
            print("%-20s %-20s" % (key, ip))

    



    

if __name__ == '__main__':
    main()
