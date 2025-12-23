# Here we will wait for 2 seconds

import asyncio

async def fetch_data(delay):
    print(f"Fetching data with a delay of {delay} seconds...")
    await asyncio.sleep(delay)  # await is to execute the coroutine and also asyncio.run() is used
    print(f"Data fetched after {delay} seconds...")
    return f"Data from {delay} seconds delay"


async def main():
    print("Start of main coroutine")
    coroutine = fetch_data(5)
    print("Coroutine created, now running...")
    result = await coroutine
    print("Coroutine completed with result : ",result)


asyncio.run(main())




