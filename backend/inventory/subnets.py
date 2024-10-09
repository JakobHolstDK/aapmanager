import redis


def main():
    r = redis.Redis(host='localhost', port=6379, db=0)
    keys = r.keys("serverinfo:netcat:*")
    for key in keys:
        server = key.decode("utf-8").split(":")[2]
        print(server)

    keys = r.keys("serverinfo:dig:*")
    for key in keys:
        server = key.decode("utf-8").split(":")[2]
        print(server)
        print(r.hgetall(key))
        


    




if __name__ == '__main__':
    main()
