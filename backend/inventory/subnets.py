import redis
import json 
import os
import sys
import time
import subprocess
import pydig
import socket
import pprint




def main():
    r = redis.Redis(host='localhost', port=6379, db=0)
    subnets = {}
    print("netcat")
    keys = r.keys("serverinfo:netcat:*")
    for key in keys:
        server = key.decode("utf-8").split(":")[2]
        value = r.get(key).decode("utf-8")

        if value == "0":
            print(server, "ssh port is open")
            dig = pydig.query(server, 'A')
            print(dig)
            for ip in dig:
                print(ip)
                try:
                    socket.inet_aton(ip)
                    print("valid ip")
                    # replace last octet with 0
                    ip = ip.rsplit(".", 1)[0] + ".0"
                    splitmyserver = server.split(".")
                    pprint.pprint(splitmyserver)
                    subnets[ip] = splitmyserver[1]
                    
                except socket.error:
                    print("invalid ip")

    
    print("subnets", subnets)
    




    




    




if __name__ == '__main__':
    main()
