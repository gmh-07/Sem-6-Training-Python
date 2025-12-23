# Here we will wait for 2 seconds

import asyncio

async def fetch_data(delay,id):
    print(f"Fetching data with a delay of {delay} seconds... for ID: {id}.........")
    await asyncio.sleep(delay)
    print(f"Data fetched after {delay} seconds... for ID: {id}.........")
    return f"Data from {delay}  seconds... for ID: {id}........."


async def main():
    print("Start of main coroutine")
    coroutine1 = fetch_data(3,1)
    print("Coroutine1 created, now running...")
    coroutine2 = fetch_data(3,2)
    print("Coroutine2 created, now running...")
    result1 = await coroutine1
    print("Coroutine1 completed with result : ","(",result1,")")
    result2 = await coroutine2

    print("Coroutine2 completed with result  : ","(",result2,")")


asyncio.run(main())




