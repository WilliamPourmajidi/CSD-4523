# Using asyncio to create a simple asynchronous application that prints messages with a delay
import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print('Hello')

async def say_goodbye():
    await asyncio.sleep(4)
    print('Goodbye')

async def main():
    await asyncio.gather(say_hello(), say_goodbye())

asyncio.run(main())

# Using asyncio to create a simple asynchronous application that prints messages with a delay