# publisher.py
import time
import redis

r = redis.Redis(host='redis', port=6379)

while True:
    message = f"send mesagge : {time.time()}"
    print(message, flush=True)
    r.publish('my-sync-channel', message)
    time.sleep(3)
