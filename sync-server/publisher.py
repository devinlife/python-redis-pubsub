# publisher.py
import redis
import time

r = redis.Redis(host='redis', port=6379, db=0)

while True:
    message = f"send mesagge : {time.time()}"
    print(message, flush=True)
    r.publish('my-channel-1', message)
    time.sleep(3)
