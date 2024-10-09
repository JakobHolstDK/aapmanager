import redis
import json 
import os
import sys
import time
import subprocess
import pydig
import socket



def main():
    r = redis.Redis(host='localhost', port=6379, db=0)

    print("netcat")
    keys = r.keys("serverinfo:netcat:*")
    for key in keys:
        server = key.decode("utf-8").split(":")[2]
        value = r.get(key).decode("utf-8")

        if value == "0":
            print(server, "ssh port is open")
            dig = pydig.query(server, 'A')
            print(dig)



    




    




if __name__ == '__main__':
    main()
