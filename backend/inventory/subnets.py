import redis


def main():
    r = redis.Redis(host='localhost', port=6379, db=0)
    keys = r.keys("serverinfo:netcat:*")
    for key in keys:
        server = key.split(":")[2]
        print(server)

    keys = r.keys("serverinfo:dig:*")
    for key in keys:
        server = key.split(":")[2]
        print(server)
        

    




if __name__ == '__main__':
    main()
