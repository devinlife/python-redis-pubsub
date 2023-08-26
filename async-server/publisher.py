import time
import asyncio

import redis.asyncio as redis


async def async_pub():
    """
    Publish a message to channel:1 every 3 seconds.
    """
    async with redis.from_url("redis://redis:6379") as r:
        try:
            while True:
                message = f"send mesagge : {time.time()}"
                await r.publish("my-async-channel", message)
                await asyncio.sleep(3)
        except redis.RedisError as error:
            print(f"Redis error occurred: {error}")


if __name__ == "__main__":
    asyncio.run(async_pub())
