import asyncio

import redis.asyncio as redis

STOPWORD = "STOP"


async def reader(channel: redis.client.PubSub):
    while True:
        message = await channel.get_message(ignore_subscribe_messages=True)
        if message is not None:
            print(f"(Reader) Message Received: {message}", flush=True)
            if message["data"].decode() == STOPWORD:
                print("(Reader) STOP")
                break


async def main():
    r = redis.from_url("redis://redis:6379")
    async with r.pubsub() as pubsub:
        await pubsub.subscribe("my-async-channel")
        await asyncio.create_task(reader(pubsub))


if __name__ == "__main__":
    asyncio.run(main())
