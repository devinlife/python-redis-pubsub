import asyncio

import redis.asyncio as redis


async def async_pub():
    """
    Publish a message to channel:1 every 3 seconds.
    """
    async with redis.from_url("redis://redis:6379") as r:
        try:
            while True:
                await r.publish("channel:1", "Hello")
                await asyncio.sleep(3)
        except redis.RedisError as e:
            print(f"Redis error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(async_pub())
