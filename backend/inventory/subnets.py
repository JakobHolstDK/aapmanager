import redis


def main():
    r = redis.Redis(host='localhost', port=6379, db=0)
    keys = r.keys("*")
    for key in keys:
        print(key)
        print(r.get(key))


if __name__ == '__main__':
    main()
